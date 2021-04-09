from typing import List
from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from fastapi import File, UploadFile
import os
from minePdf import pdf_all

# pyttsx3
# espeak
# fastapi
# ffmpeg
app = FastAPI()


@app.post("/pdf_initialize")
async def pdfToText(byteFile: UploadFile = File(...)):
    path = os.getcwd() + "/saved_pdf/" + byteFile.filename
    with open(path, "ab") as f:
        for chunk in iter(lambda: byteFile.file.read(10000), b""):
            f.write(chunk)

    # Do things with file here
    # Save text as a _string
    await pdf_all(byteFile.filename)
    # Uncomment this statement and comment out the test return

    # return{"text":_string}
    return {
        "filename": byteFile.filename,
        "content-type": byteFile.content_type,
        "file": byteFile.file,
    }


@app.post("get_summary")
async def returnSummary(filename: str):
    if filename[:-4] == ".pdf":
        filename = filename[:-4]
    return FileResponse("./saved_summary/" + filename + ".txt")


@app.post("get_text")
async def returnTxt(filename: str):
    if filename[:-4] == ".pdf":
        filename = filename[:-4]
    return FileResponse("./saved_txt/" + filename + ".txt")


@app.post("get_mp3")
async def returnMp3(filename: str):
    if filename[:-4] == ".pdf":
        filename = filename[:-4]
    return FileResponse("./saved_mp3/" + filename + ".txt")
