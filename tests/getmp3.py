# Used to get mp3 from server
import requests
from io import BytesIO

url = "http://127.0.0.1:8000/get_mp3"
pdf = "r1.pdf"
files = {"filename": pdf}
r = requests.get(url, params=files)
print(r)