from requests import *
from re import *
url = input()
url_request = get(url)
print(findall(r'<h3\b[^>]*>(.*?)<\/h3>', url_request.text))
