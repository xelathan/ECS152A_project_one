import requests

# Define the URL and custom headers
url = 'https://kartik-labeling-cvpr-0ed3099180c2.herokuapp.com/ecs152a_ass1'
headers = {'Student-Id': '919196458'}

# Configure MITMProxy to intercept requests
# Make sure MITMProxy is running on your local machine
# You may need to set up MITMProxy to capture and inspect the request/response

# Disable SSL certificate verification
proxies = {
    'http': 'http://127.0.0.1:8080',  # Change to your MITMProxy's listening address
    'https': 'http://127.0.0.1:8080',  # Change to your MITMProxy's listening address
}

# Send the GET request with custom headers and SSL verification disabled
response = requests.get(url, headers=headers, proxies=proxies, verify=False)

# Print the response
print("Headers:", response.headers)
