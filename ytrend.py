
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
while con == True:
      list1=[]
      for link in soup.find_all("h3",{"class":"yt-lockup-title"}):
          for var in link.find_all("a"):
              title = var.get("title")
              href = var.get("href")
              print("Title[%s] = %s\n"%(i,title))
              list1.insert(i,href)
              i=i+1

      choice = int(raw_input("Enter your choice of video or press -1 "))
      select =list1[choice]
      link = "https://www.youtube.com"+select
      
      if choice!=-1:
         option = raw_input("VLC(v) or Youtube(y) ")
         if option=='y':
            webbrowser.open(link)
         else:
            myprocess = subprocess.call(['vlc','-vvv',link])
      choice=raw_input("Want to continue y/n ")
      if choice=='n':
         con=False
      i=0   
