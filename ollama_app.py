import requests
import json
import re

def get_available_get_requests(base_url):
    try:
        response = requests.get(base_url)
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text:\n{response.text}")  
        print("Response Headers:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")

        if response.status_code == 200:
            print("Available GET requests:")
            links = re.findall(r'href=[\'"]?([^\'" >]+)', response.text)
            if not links:  
                print("No links found in the response text.")
            for link in links:
                if link.startswith('/api/'):
                    print(link)
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def get_header_options(base_url, endpoint):
    try:
        full_url = base_url + endpoint
        response = requests.options(full_url)
        if response.status_code == 200:
            print(f"\nHeader options for {endpoint}:")
            print("Request Headers:")
            for key, value in response.request.headers.items():
                print(f"{key}: {value}")
            print("Response Headers:")
            for key, value in response.headers.items():
                print(f"{key}: {value}")
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def send_post_request(base_url, endpoint):
    try:
        full_url = base_url + endpoint
        headers = {
            'mode' : 'GET , POST, GET',
            
            'Content-Type': 'application/json',
            
        }
        data = {'message': 'Hello, world!'}  # Replace with your actual payload
        response = requests.post(full_url, headers=headers, json=data)
        if response.status_code == 200:
            print(f"\nPOST request to {endpoint} successful!")
        else:
            print(f"Error: {response.status_code}")
        
        print("Request Headers:")
        for key, value in response.request.headers.items():
            print(f"{key}: {value}")
        print("Response Headers:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")
        print(f"Cookies: {response.cookies}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def send_get_request(base_url, endpoint):
    try:
        full_url = base_url + endpoint
        headers = {
            'mode' : 'GET',
            'Content-Type': 'application/json',
            # Add any other required headers here
        }
        response = requests.get(full_url, headers=headers)
        if response.status_code == 200:
            print(f"\nGET request to {endpoint} successful!")
        else:
            print(f"Error: {response.status_code}")
        
        print("Request Headers:")
        for key, value in response.request.headers.items():
            print(f"{key}: {value}")
        print("Response Headers:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")
        print(f"Cookies: {response.cookies}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def main():
    base_url = 'http://localhost:2222'
    get_available_get_requests(base_url)
    endpoint = '/api/chat'
    get_header_options(base_url, endpoint)
    send_post_request(base_url, endpoint)
    send_get_request(base_url, endpoint)

if __name__ == "__main__":
    main()
