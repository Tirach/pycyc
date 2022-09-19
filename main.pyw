# Imports
import requests
import time
from datetime import datetime

# Main function


def main():
    while True:
        dt = datetime.now()
        try:
            requests.get(url, timeout=timeout)
            print(f'Connected to the internet at {dt}')
        except (requests.ConnectionError, requests.Timeout):
            f = open('Dropouts.txt', 'a')
            f.write(f'\nNo internet connection at {dt}\n')
            f.close()
        time.sleep(60.0 - ((time.time() - starttime) % 60.0))

        
# Set variables
url = "https://www.google.com/"
timeout = 5
starttime = time.time()

# Call main function
main()
