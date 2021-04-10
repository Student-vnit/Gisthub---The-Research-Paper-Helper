from typing import List
from fastapi import FastAPI, Query, BackgroundTasks
from fastapi.responses import FileResponse
from fastapi import File, UploadFile, Request
import os
from minePdf import pdf_all, init_audio
from fastapi.middleware.cors import CORSMiddleware

# from reportlab.pdfgen.canvas import Canvas

# pyttsx3
# espeak
# fastapi
# ffmpeg
app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.on_event("startup")
# async def startup_event():
#     model = T5ForConditionalGeneration.from_pretrained("t5-base")
#     # # initialize the model tokenizer
#     tokenizer = T5Tokenizer.from_pretrained("t5-base")


@app.post("/pdf_initialize")
async def pdfToText(
    background_tasks: BackgroundTasks, byteFile: UploadFile = File(...)
):
    path = "./saved_pdf/" + byteFile.filename
    with open(path, "w") as f:
        f.write("")

    with open(path, "ab") as f:
        for chunk in iter(lambda: byteFile.file.read(10000), b""):
            f.write(chunk)
    # background_tasks.add_task(init_summary, byteFile.filename)
    background_tasks.add_task(pdf_all, byteFile.filename)
    background_tasks.add_task(init_audio, byteFile.filename)

    # await pdf_all(byteFile.filename)
    # await init_audio(byteFile.filename)
    return {
        "filename": byteFile.filename,
        "content-type": byteFile.content_type,
        "file": byteFile.file,
    }


@app.post("/test_formdata")
async def formdata(byteFile: UploadFile = File(...)):
    print(byteFile.filename)
    return {"status": "done"}


@app.post("/get_summary")
async def returnSummary(filename: str):
    if filename[-4:] == ".pdf":
        filename = filename[:-4]
    file_path = os.path.join("./", "saved_summary/" + filename + ".txt")
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"Error": "Summary not found!"}


@app.post("/get_text")
async def returnTxt(filename: str):
    if filename[-4:] == ".pdf":
        filename = filename[:-4]
    file_path = os.path.join("./", "saved_txt/" + filename + ".txt")
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"Error": "Text not found!"}


@app.post("/get_mp3")
async def returnMp3(filename: str):
    if filename[-4:] == ".pdf":
        filename = filename[:-4]
    file_path = os.path.join("./", "saved_mp3/" + filename + ".mp3")
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"Error": "Mp3 not found!"}


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=environ.get("PORT", 8000))
