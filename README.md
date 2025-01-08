# Varun_Raj_fetchround1
# Health Check Script

## Overview
This project implements a health check script that monitors the availability of a set of HTTP endpoints. The script reads a configuration file in YAML format, performs health checks on the specified endpoints every 15 seconds, and logs the availability percentage to the console. The script runs indefinitely until the user stops it manually.

## File Structure

- **requirements.txt**: Lists the required Python packages.
- **health_check.py**: The main script that performs the health checks.
- **config.yaml**: The configuration file containing the list of HTTP endpoints to monitor.

## Desired Output
The script logs the availability percentage of each URL domain over the lifetime of the program to the console. The availability percentage is calculated as:
```
Availability Percentage = 100 * (Number of UP requests / Total number of requests)
```
Example output:


<img width="624" alt="image" src="https://github.com/user-attachments/assets/8f6ce039-96f7-4dd8-a3c0-1e81b95e53cd" />

```

## Prerequisites
Before running the script, ensure you have Python and pip installed on your system. You can check if they are installed by running:
```bash
python --version
pip --version
```
If they are not installed, please install them from the official Python website: https://www.python.org/

## Installing Requirements
To install the required packages listed in `requirements.txt`, run the following command:
```bash
pip install -r requirements.txt
```

## Running the Code
To run the health check script, follow these steps:
1. Open a terminal and navigate to the project directory.
2. Run the script:
   ```
   python health_check.py
   ```
3. When prompted, enter the path to the configuration file, e.g., `/path/to/config.yaml`.

## Stopping the Script
To stop the script, press `Ctrl + C` in the terminal where the script is running. This will terminate the script and stop the health checks.

## Changing the Configuration File
To change the configuration file:
1. Open the `config.yaml` file in a text editor.
2. Modify the list of HTTP endpoints as needed.
3. Save the changes.
4. or simply, add a new file, and give the appropriate path to the new file when prompted. 
5. Restart the script to apply the new configuration.






