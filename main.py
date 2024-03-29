import os
import requests

def main():
    response = requests.get('https://debug.enzoguard.com/ip')
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error: Received status code {response.status_code}")

if __name__ == "__main__":
    main()
