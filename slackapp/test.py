import requests

# Replace this URL with the actual URL where your Flask app is running
API_URL = "http://localhost:5000/agent"

# Sample JSON payload
json_payload = {
    "email": "keviinkibe@gmail.com",
    "message": "send an email to kchegz234@gmail.com wishing him a good day"
}

# Send a POST request to the API
response = requests.post(API_URL, json=json_payload)

# Print the API response
print("API Response:")
print(response.text)
