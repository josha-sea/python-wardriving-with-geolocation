'''

Test-Script using requests and bs4 with the website https://www.where-am-i.co/

Note: Does not work

'''

# Imports
import requests
from bs4 import BeautifulSoup

url = "https://www.where-am-i.co/"

res = requests.get(url)

soup = BeautifulSoup(res.content, 'html.parser')

with open("where.html", "w") as f:
	f.write(str(soup))