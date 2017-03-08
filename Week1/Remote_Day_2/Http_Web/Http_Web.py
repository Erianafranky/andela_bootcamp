import requests

request = requests.get('http://anapioficeandfire.com/api/')
print(request.text)