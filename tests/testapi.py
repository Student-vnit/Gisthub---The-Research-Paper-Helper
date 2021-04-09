import requests
from io import BytesIO

pdfpath = "/home/abhk943/Documents/vnitSem6/softLabTTS/r1.pdf"
url = "http://127.0.0.1:8000/pdf_initialize"
pdf = open(pdfpath, "rb")
files = {"byteFile": pdf, "filename": pdfpath}
r = requests.post(url, files=files)
print(r.text)
