import requests

request = requests.get('http://anapioficeandfire.com/api/houses/378')
request.status_code
print(request.text)
print (request.headers['content-type'])