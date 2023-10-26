import requests
url = 'https://kartik-labeling-cvpr-0ed3099180c2.herokuapp.com/ecs152a_ass1'
response = requests.get(url, headers={'Student-Id': '919196458'}, verify=False)

print(response.headers)