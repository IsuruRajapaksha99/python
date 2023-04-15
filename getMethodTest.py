import requests
r= requests.get('https://www.youtube.com/')
print(r.status_code)
print(r.url)
print(r.text)