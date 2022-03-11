import requests
import os
import wget

url = "https://www.reddit.com/r/wallpapers/.json"

response = requests.get(url).json()

response = response["data"]["children"]

urls= []
for post in response:
    try:
        urls.append(post["data"]["url"])
    except:
        continue

print(urls)

download = input("Download all? (y to do it)")
if download.lower() not in ["y", "yes"]:
    quit()

for url in urls:
    try:
        os.mkdir("downloads")
    except FileExistsError:
        pass
    
    wget.download(url, out="downloads/")