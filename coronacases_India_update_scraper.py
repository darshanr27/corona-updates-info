import requests
from bs4 import BeautifulSoup

url="https://www.worldometers.info/coronavirus/country/india/"
page=requests.get(url)

info=BeautifulSoup(page.text, 'html.parser')
cases=info.find_all("div", class_="maincounter-number")

print("Total Coronvirus cases:",cases[0].text.strip())
print("Deaths:",cases[1].text.strip())
print("Recovered:",cases[2].text.strip())