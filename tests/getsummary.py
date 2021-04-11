# Used to get summary from server
import requests
from io import BytesIO
import os

url = "http://f3eebc66f3a5.ngrok.io"
content = ""
file_path = "/home/abhk943/Documents/vnitSem6/Gisthub---The-Research-Paper-Helper/saved_txt/r1.txt"
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        content = f.read()
files = {"text": content}
r = requests.post(url, data=files)
print(r.text)
