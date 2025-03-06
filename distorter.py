import os
from pydub import AudioSegment
import time

# Reduces bitrate of the audio file
def makeAudioSoundBad(audio: AudioSegment, filePath: str) -> AudioSegment:
    filePath = filePath.replace("\\", "/")
    fileDir = os.path.dirname(filePath)
    newFileName = input("Enter the resulting file name:\n")
    if not newFileName.endswith(".mp3"):
        newFileName += ".mp3"
    newAudioPath = os.path.join(fileDir, newFileName)
    newAudioFile = audio.export(newAudioPath, format="mp3", bitrate="4k")
    print("file saved as " + fileDir + newFileName)
    return newAudioFile

filePath = input("Enter the file path (and name)\n(must be an mp3): ")
filePath = filePath.replace('"', '')
if os.path.exists(filePath):
    audio = AudioSegment.from_mp3(filePath)
    badAudio = makeAudioSoundBad(audio, filePath)
    print("The worsened file is in the same directory as the original!")
else:
    print("Invalid file/directory")
time.sleep(5)