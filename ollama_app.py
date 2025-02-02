import requests
import json
import re

def get_available_get_requests(base_url):
    try:
        response = requests.get(base_url)
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text:\n{response.text}")  # Print the response text for debugging purposes

        if response.status_code == 200:
            print("Available GET requests:")
            links = re.findall(r'href=[\'"]?([^\'" >]+)', response.text)
            if not links:  # Check if any links were found
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
            print("Allowed methods:", response.headers.get('Allow'))
            print("Allowed headers:", response.headers.get('Access-Control-Allow-Headers'))
            print("Content-Type:", response.request.headers.get('Content-Type'))
            print("Response headers:")
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
            'mode' : 'POST',
            'Content-Type': 'application/json',
            # Add any other required headers here
        }
        data = {'message': 'Hello, world!'}  # Replace with your actual payload
        response = requests.post(full_url, headers=headers, json=data)
        if response.status_code == 200:
            print(f"\nPOST request to {endpoint} successful!")
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def send_get_request(base_url, endpoint):
    try:
        full_url = base_url + endpoint
        response = requests.get(full_url)
        if response.status_code == 200:
            print(f"\nGET request to {endpoint} successful!")
            print(response.json())
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def main():
    base_url = "http://localhost:2222"
    get_available_get_requests(base_url)

    endpoint = "/api/chat"
    get_header_options(base_url, endpoint)
    send_post_request(base_url, endpoint)

    endpoint = "/api/tags"
    send_get_request(base_url, endpoint)

if __name__ == "__main__":
    main()

# print(response.headers)

# print(response.status_code)

# import requests

# def try_endpoint(url):
#     try:
#         response = requests.options(url)
#         print(f"URL: {url}")
#         print(response.headers)
#         print(response.text)
#     except requests.exceptions.RequestException as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     endpoints = [
#         "http://localhost:2222/",
#         "http://localhost:2222/api/chat",
#         "http://localhost:2222/api/tags",
#         "http://localhost:2222/api/messages"
#     ]

#     for endpoint in endpoints:
#         try_endpoint(endpoint)
