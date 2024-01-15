import os
import requests

def main():
    proxy_url = os.getenv('HTTPS_PROXY')
    proxies = {'https': proxy_url} if proxy_url else None

    response = requests.get('https://debug.enzoguard.com/ip', proxies=proxies)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error: Received status code {response.status_code}")

if __name__ == "__main__":
    main()
