from typing import List
from fastapi import FastAPI, Query, BackgroundTasks
from fastapi.responses import FileResponse
from fastapi import File, UploadFile, Request
import os
from minePdf import pdf_all, init_audio, init_summary
from fastapi.middleware.cors import CORSMiddleware
import time

app = FastAPI()

# Adding CORS as middleware
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Saves the uploaded PDF file and starts background tasks for text, audio, summary conversion
@app.post("/pdf_initialize")
async def pdfToText(
    background_tasks: BackgroundTasks, byteFile: UploadFile = File(...)
):
    path = "./saved_pdf/" + byteFile.filename

    # Creating an empty pdf file
    with open(path, "w") as f:
        f.write("")

    # Appending to file chunk by chunk
    with open(path, "ab") as f:
        for chunk in iter(lambda: byteFile.file.read(10000), b""):
            f.write(chunk)

    # URL for ngrok server running at colab, to serve summary
    url = "http://28095768d382.ngrok.io"

    # background_task for text, audio, summary, runs after return
    background_tasks.add_task(pdf_all, byteFile.filename)
    background_tasks.add_task(init_summary, byteFile.filename, url)
    background_tasks.add_task(init_audio, byteFile.filename)

    # Return received file's details
    return {
        "filename": byteFile.filename,
        "content-type": byteFile.content_type,
        "file": byteFile.file,
    }


# test api created for testing file upload
@app.post("/test_formdata")
async def formdata(byteFile: UploadFile = File(...)):
    print(byteFile.filename)
    return {"status": "done"}


# Get summary from stored location as FileResponse
@app.post("/get_summary")
async def returnSummary(filename: str):
    if filename[-4:] == ".pdf":
        filename = filename[:-4]
    file_path = os.path.join("./", "saved_summary/" + filename + ".txt")
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"Error": "Summary not found!"}


# Get text from stored location as FileResponse
@app.post("/get_text")
async def returnTxt(filename: str):
    if filename[-4:] == ".pdf":
        filename = filename[:-4]
    file_path = os.path.join("./", "saved_txt/" + filename + ".txt")
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"Error": "Text not found!"}


# Get mp3 from stored location as FileResponse
@app.get("/get_mp3")
async def returnMp3(filename: str):
    if filename[-4:] == ".pdf":
        filename = filename[:-4]
    file_path = os.path.join("./", "saved_mp3/" + filename + ".mp3")
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"Error": "Mp3 not found!"}


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=environ.get("PORT", 8000))
