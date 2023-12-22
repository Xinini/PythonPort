import ctypes
import os
import config
import praw
import requests
from PIL import Image

#Identification from config.py
CLIENT_ID = config.clientID
CLIENT_SECRET = config.clientSecret
USERNAME = config.username
PASSWORD = config.password
USER_AGENT = "RedditWallScraperz"

#ctypes parameter idk
SPI_SETDESKWALLPAPER = 20 


def save_image(url, filename):
    data = requests.get(url).content
    f = open (filename, "wb")
    f.write(data)
    f.close()
    #img = Image.open("img.png")
    #img.show()  


#Making a reddit instance
reddit = praw.Reddit(client_id = CLIENT_ID,
                     client_secret = CLIENT_SECRET,
                     username = USERNAME,
                     password = PASSWORD,
                     user_agent = USER_AGENT
                     )
#Get posts from wallpaper sub
wallpapper_sub = reddit.subreddit(display_name="wallpaper").top(time_filter = "day", limit=10)

#Make recurssion?
for post in wallpapper_sub:
    file_ext = post.url.split("/")[-1].split(".")[-1]
    if not post.stickied:
        if file_ext == "png" or file_ext == "jpg":
            print(post.title + " " + post.url)
            filename =  post.title + "." + file_ext
            print(file_ext)
            save_image(post.url, filename)
            break


print(filename)
path = os.getcwd() + "\\" + filename
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , 0)
