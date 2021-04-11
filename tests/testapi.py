# Used to upload a pdf file and start its conversion
import requests
from io import BytesIO

pdfpath = "/home/abhk943/Documents/vnitSem6/softLabTTS/r1.pdf"
url = "https://gisthub-vnit.herokuapp.com/pdf_initialize"
pdf = open(pdfpath, "rb")
files = {"byteFile": pdf, "filename": pdfpath}
r = requests.post(url, files=files)
print(r.text)
