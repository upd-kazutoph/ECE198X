import os
from pydub import AudioSegment
#INSTALL FFMPEG USING APT INSTALL FOR PYDUB SUPPORT

path = "dataset_ref/audio" #ENTER INPUT PATH HERE (also output path)

os.chdir(path)
audio_files = os.listdir()

for file in audio_files: #Make sure to get all files inside the folder/path
    name, ext = os.path.splitext(file)
    if ext == ".mp3":
       mp3_sound = AudioSegment.from_mp3(file)
       mp3_sound.export("{0}.wav".format(name), format="wav") #change extension (with same filename)