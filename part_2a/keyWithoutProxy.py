import requests

url = 'https://kartik-labeling-cvpr-0ed3099180c2.herokuapp.com/ecs152a_ass1'
headers = {'Student-Id' : '919508305'}

response =  requests.get(url, headers = headers)

print(response.headers)
