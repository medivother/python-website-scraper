import requests
from bs4 import BeautifulSoup
import json

login_url = ['xxxxxxxxxxxx']

payload = {
    'password': 'xxxxxxxxxxxxxxx',
    'username': 'xxxxxxxxxxxxxxx'
}
with requests.session() as s:       #this will maintain the log in so that you can do multiple requests to the secured pages
    s.post(login_url,data=payload)  
