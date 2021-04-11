# Used to get text from server
import requests
from io import BytesIO

url = "https://gisthub-vnit.herokuapp.com/get_text"
pdf = "r1.pdf"
files = {"filename": pdf}
r = requests.post(url, params=files)
print(r.text)
