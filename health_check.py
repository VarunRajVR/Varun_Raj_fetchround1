import yaml
import time
import requests


class HealthCheck:

    # defining a constructor.
    def __init__(self, file_path):
        #handling missing path.
        if not file_path:
            raise ValueError("file_path cannot be None")
        
        #getting the path of the file from user. 
        self.file_path = file_path
        self.config = self.read_config(self.file_path)

        #validating the input.
        if self.config is None:
            raise ValueError("Invalid configuration file.")
        
        #creating a dictionary to store the status of endpoints.
        self.results = {config['url']: {'up': 0, 'total': 0} for config in self.config} 

    # function reads the config file AND returns endpoints. 
    def read_config(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = yaml.load(file, Loader=yaml.SafeLoader)
            return data
        except FileNotFoundError:
            print(f"Configuration file not found: {file_path}")


    def status_check(self):

        # API ends when user gives ctrl C.
        while True:
            for endpoint in self.config: # for each endpoint.
                url = endpoint['url']
                method = endpoint.get('method', 'GET')
                headers = endpoint.get('headers', {})
                body = endpoint.get('body', None)

                # defining all the http methods in a dictionary to handle them dynamically.
                try:
                    method_function = {
                        'GET': requests.get,
                        'POST': requests.post,
                        'PUT': requests.put,
                        'DELETE': requests.delete,
                        'PATCH': requests.patch,
                        'HEAD': requests.head,
                        'OPTIONS': requests.options
                    }.get(method)

                    if method_function:
                        response = method_function(url, headers=headers, data=body, timeout=0.5)
                    else:
                        continue

                    latency = response.elapsed.total_seconds() * 1000  # Convert to milliseconds

                    # check for status and latency constraints. 
                    if 200 <= response.status_code < 300 and latency < 500:
                        self.results[url]['up'] += 1
                    self.results[url]['total'] += 1

                # if down, just increase the total count. 
                except requests.RequestException:
                    self.results[url]['total'] += 1
            
            self.log_results()
            #running the app every 15 seconds.
            time.sleep(15)
        
        return

    def log_results(self):
        
        # logging the results and printing them. 
        for url, data in self.results.items():
            availability = 100 * (data['up'] / data['total'])
            print(f"{url} has {round(availability)}% availability percentage")



if __name__ == "__main__":
    file_path = input("Enter the path to the YAML file: ")
    health_check = HealthCheck(file_path)
    try:
        health_check.status_check()
    except KeyboardInterrupt:
        print("Hppy Health checking.")

