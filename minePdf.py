import fitz
import json
import re
from collections import defaultdict
from fitz.fitz import getTextlength
from segment import viterbi
import pyttsx3
from gtts import gTTS
import os
import copy
import time
import requests

# Used to threshold paragrams to remove headers, footers and irrelevant text
def frequencyThreshold(ans):
    f = defaultdict(int)
    newans = []
    for block in ans:
        f[block[0]] += block[2]
    threshold = max(f, key=lambda x: f[x])
    for block in ans:
        if threshold <= block[0]:
            newans.append(block[1])
    return "\n".join(newans)


# Initializes audio from textfile
async def init_audio(filename):
    time.sleep(10)
    print("Init Audio started")
    content = ""
    if filename[-4:] == ".pdf":
        filename = filename[:-4]
    file_path = os.path.join("./", "saved_txt/" + filename + ".txt")
    audio_path = os.path.join("./", "saved_mp3/" + filename + ".mp3")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            content = f.read()
    contentD = copy.deepcopy(content)
    # speaker = pyttsx3.init()
    # speaker.save_to_file(contentD, audio_path)
    # speaker.runAndWait()

    # Using googleTextToSpeech to save audio
    myobj = gTTS(text=contentD, lang="en", slow=False)
    myobj.save(audio_path)
    print("Audio Saved: {}\n".format(audio_path))


# Initializes summary from textfile
async def init_summary(filename, url):
    time.sleep(10)
    content = ""
    print("Init summary started")
    if filename[-4:] == ".pdf":
        filename = filename[:-4]
    file_path = os.path.join("./", "saved_txt/" + filename + ".txt")
    summary_path = os.path.join("./", "saved_summary/" + filename + ".txt")

    # Sends text to colab->ngrok server and receives summarized text
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            content = f.read()
    files = {"text": content}
    r = requests.post(url, data=files)

    # Writing received text to file
    try:
        with open(summary_path, "w") as f:
            f.write(r.text)
    except IOError as e:
        print(e)
    print("Summary saved: {}\n".format(summary_path))


# Initialized text file from pdf
async def pdf_all(filename):
    doc = fitz.open("./saved_pdf/" + filename)
    ans = []
    flag = 1
    for index in range(0, doc.page_count):
        page1 = doc.load_page(index)
        text = page1.get_text("json")
        jtext = json.loads(text)

        for block in jtext["blocks"]:
            if "lines" in block.keys():
                # print("----")
                str = ""
                size = block["lines"][0]["spans"][0]["size"]
                for line in block["lines"]:
                    for li in line["spans"]:
                        str = str + li["text"]

                # data cleaning
                str = str.lower()
                str.replace("\n", " ")
                st = re.sub(r"\. ", ". \n", str)
                st = re.sub(r"^https?:\/\/.*[\r\n]*", "", st, flags=re.MULTILINE)
                st = re.sub(r"\.( )*", ". \n", st)
                st = re.sub(r"( )*-( )*", "", st)
                st = re.sub(r"\d+\. \n", "", st)
                st = re.sub(r"\[[0-9]+\]", "", st)

                # print("st",st)
                numlines = len(list(st.split("\n")))
                correctedSentence = []
                for line in list(st.split("\n")):
                    correctedWords = []
                    if line:
                        wordCount = len(list(line.split(" ")))
                        for word in list(line.split(" ")):
                            vt = viterbi(word)[1]
                            if (
                                vt
                                and vt[0] == "references"
                                and numlines == 1
                                and wordCount <= 2
                            ):
                                flag = 0
                                break
                            correctedWords += vt
                        # print("CW", correctedWords)
                        if flag == 0:
                            break
                        correctedWords = " ".join(correctedWords)
                        correctedSentence.append(correctedWords)
                if flag == 0:
                    break

                st = "\n".join(correctedSentence)
                ans.append((size, st, numlines))

            if flag == 0:
                break
        if flag == 0:
            break

    ans = frequencyThreshold(ans)
    try:
        with open("./saved_txt/" + filename[:-4] + ".txt", "w") as f:
            f.write(ans)
    except IOError as e:
        print(e)
    print("Text saved: {}\n".format("./saved_txt/" + filename[:-4] + ".txt"))
