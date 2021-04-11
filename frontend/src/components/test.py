import requests
from io import BytesIO

pdfpath = "assignment.pdf"
url = "https://gisthub-vnit.herokuapp.com/pdf_initialize"
pdf = open(pdfpath, "rb")
files = {"byteFile": pdf, "filename": pdfpath}
r = requests.post(url, files=files)
print(r.text)