import requests
from io import BytesIO

url = "https://gisthub-vnit.herokuapp.com/get_mp3"
pdf = "r1.pdf"
files = {"filename": pdf}
r = requests.post(url, params=files)
import pydub
from pydub import AudioSegment
from pydub.playback import play
import io

song = AudioSegment.from_file(io.BytesIO(r.content), format="mp3")
play(song)
song.export("./filename.mp4", format="mp3")
