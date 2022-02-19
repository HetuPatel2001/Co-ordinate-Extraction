import time
import pandas as pd
from selenium import webdriver

links = []
urls = []
Address = []
latitude = []
longitude = []

driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver_win32\chromedriver.exe")
data = pd.read_excel(r"C:\Users\Hetu Prakash Patel\Downloads\Book1.xlsx")
data.head()
address = data['Address']
for i in address:
  Address.append(i)
  link = "https://www.google.com/maps/search/"+ i
  links.append(link)


for link in links:
  urL = link
  driver.get(urL)
  time.sleep(10)
  get_url = driver.current_url
  urls.append(get_url)


for url in urls:
  pos = url.split("@")
  coord = pos[1].split(",")
  lat = coord[0]
  latitude.append(lat)
  long = coord[1]
  longitude.append(long)

df = pd.DataFrame({'Address': Address,
                   'URL': urls,
                   'Latitude': latitude,
                   'Longitude': longitude})

df.to_csv("data.csv")