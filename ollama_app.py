import json
import requests

if __name__ == "__main__":
    url = "http://localhost:2222/api/tags"
    response = requests.get(url)

    if response.status_code == 200:
        model_response = response.json()
        print("Available Models:")
        for model in model_response:
            print(f"Name:{model['name']}")
            print(f"Desctiption:{model['description']}")
            print(f"Tags:{mode['tags']}")
            print()
    else:
        print(f"Error: {response.status_code}")

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
