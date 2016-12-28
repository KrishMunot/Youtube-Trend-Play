#Play Trending Videos

from bs4 import BeautifulSoup
import requests
import webbrowser
import subprocess

response = requests.get("https://www.youtube.com/feed/trending")

data = response.text
soup = BeautifulSoup(data,"lxml") 

#get all header tags

i=0 
con = True
while con==True:
      list1=[]
      for link in soup.find_all("h3",{"class":"yt-lockup-title"}):
          for var in link.find_all("a"):
              title = var.get("title")
              href  = var.get("href")
              print("Title[%s] = %s\n"%(i,title))
              list1.insert(i,href)
              i=i+1
      
      choice = int(raw_input("Want to play video enter your choice else -1 "))
      select = list1[choice]
      link = "https://www.youtube.com" + select
