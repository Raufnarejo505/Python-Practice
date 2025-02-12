# In python, libraries like Requests and urllib3 let you manipulate HTTP requests easilty and efficiently
#  just by calling an apporpriate method and passing the required parameters in to it

# import requests
# PARAMS = {'bibkeys':'ISBN:1718500521','format':'json'}
# requests.get('http://openlibrary.org/api/books',params=PARAMS)
import json
import urllib3
http = urllib3.PoolManager()

# r = http.request('GET','https://github.com/pythondatabook/sources/blob/main/ch4/excerpt.txt')
# for i, line in enumerate(r.data.decode('utf-8').split('\n')):
#     if line.strip():
#         print("Line %i: " %(i), line.strip())

# print(r.data)

# API request with urllib3 to access articles about python proograming from newapi wesbite
API_KEY = '989c5c91674641879751a81baf5a9239'
# r = http.request('GET',url = "https://newsapi.org/v2/everything?q=Python programming language&apiKey=989c5c91674641879751a81baf5a9239&pageSize=5")
# articles = json.loads(r.data.decode('utf-8'))
# for article in articles['articles']:
#     print(article['title'])
#     print(article['publishedAt'])
#     print(article['url'])
#     print()

import requests
r = requests.get("https://newsapi.org/v2/everything?q=Python programming language&apiKey=989c5c91674641879751a81baf5a9239&pageSize=5")
for i, line in enumerate(r.text.split('\n')):
    if line.strip():
        print("Line %i: ", line.strip())



