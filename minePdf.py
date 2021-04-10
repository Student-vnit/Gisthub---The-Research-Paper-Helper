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


def frequencyThreshold(ans):
    f = defaultdict(int)
    newans = []
    for block in ans:
        f[block[0]] += block[2]
    # print(f)
    threshold = max(f, key=lambda x: f[x])
    for block in ans:
        if threshold <= block[0]:
            newans.append(block[1])
    return "\n".join(newans)


async def init_audio(filename):
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

    myobj = gTTS(text=contentD, lang="en", slow=False)
    myobj.save(audio_path)
    print("Audio Saved: {}\n".format(audio_path))


# async def init_summary(filename):
# if filename[-4:] == ".pdf":
#     filename = filename[:-4]
# file_path = os.path.join("./", "saved_txt/" + filename + ".txt")
# summary_path = os.path.join("./", "saved_summary/" + filename + ".txt")
# text = ""
# f = open(file_path, mode="r", encoding="utf-8")
# for line in f:
#     text = text + str(line) + "\n"

# response = []
# lines = list(text.split("\n"))
# cnt = 0
# abstractive_summary = ""
# if len(lines) > 200:
#     final_summary = ""
#     threshold_lines = 200
#     while cnt < len(lines):
#         sub_str = lines[cnt : min(cnt + threshold_lines, len(lines))]
#         sub_str = "\n".join(sub_str)
#         inputs = tokenizer.encode(
#             "summarize: " + sub_str,
#             return_tensors="pt",
#             max_length=512,
#             truncation=True,
#         )
#         outputs = model.generate(
#             inputs,
#             max_length=700,
#             min_length=100,
#             length_penalty=2.0,
#             num_beams=4,
#             early_stopping=True,
#         )
#         abstractive_summary = abstractive_summary + tokenizer.decode(outputs[0])
#         cnt = cnt + threshold_lines
# else:
#     print("abstractive only")
#     final_summary = text
#     inputs = tokenizer.encode(
#         "summarize: " + final_summary,
#         return_tensors="pt",
#         max_length=512,
#         truncation=True,
#     )
#     outputs = model.generate(
#         inputs,
#         max_length=700,
#         min_length=100,
#         length_penalty=2.0,
#         num_beams=4,
#         early_stopping=True,
#     )

#     abstractive_summary = tokenizer.decode(outputs[0])
# with open(summary_path, "w") as f:
#     f.write(abstractive_summary)
# print("summary done")


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
    print("textdone")
    # speaker = pyttsx3.init()
    # speaker.save_to_file(ans, "./saved_mp3/" + filename[:-4] + ".mp3")
    # speaker.runAndWait()

    # myobj = gTTS(text=ans, lang="en", slow=False)
    # myobj.save("./saved_mp3/" + filename[:-4] + ".mp3")
    # print("saved")
    # print(ans)
    # print("\n")


# if __name__ == "__main__":
#     pdf_all("r1.pdf")