import requests

request = requests.get('http://anapioficeandfire.com/api/')
print (request.status_code)
if request.status_code != 200:
	print ("Error: Please refresh request")
else:
	print (request.text)
print (request.headers['content-type'])
