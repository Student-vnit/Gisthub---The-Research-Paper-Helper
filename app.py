from typing import List
from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from fastapi import File, UploadFile
import os

app = FastAPI()
@app.post("/pdfToText")
async def pdfToText(byteFile:UploadFile=File(...)):
    path=os.getcwd()+"/saved_pdf/"+byteFile.filename
    with open(path, 'ab') as f:
        for chunk in iter(lambda: byteFile.file.read(10000), b''):
            f.write(chunk)

    # Do things with file here
    # Save text as a _string

    # Uncomment this statement and comment out the test return

    # return{"text":_string}
    return {"filename":byteFile.filename,"content-type":byteFile.content_type,"file":byteFile.file}