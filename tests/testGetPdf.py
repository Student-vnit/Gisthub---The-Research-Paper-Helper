import requests
from io import BytesIO

url = "http://127.0.0.1:8000/get_text"
pdf = "r1.pdf"
files = {"filename": pdf}
r = requests.post(url, params=files)
print(r.text)
