import os
from pydub import AudioSegment
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Audio Distorter")
root.geometry("400x200")

def newAudioFile(audio: AudioSegment, filePath: str, newFileStringVar: tk.StringVar, window: tk.Toplevel):
    newFileName = newFileStringVar.get()
    if not newFileName.endswith(".mp3"):
        newFileName += ".mp3"
    filePath = filePath.replace("\\", "/")
    fileDir = os.path.dirname(filePath)
    newAudioPath = os.path.join(fileDir, newFileName)
    audio.export(newAudioPath, format="mp3", bitrate="16k")
    messagebox.showinfo(title="Success", message="file saved as " + fileDir + "/" + newFileName)
    window.destroy()


def fileInputWindow(audio: AudioSegment, filePath: str):
    window = tk.Toplevel(root)
    window.title("Enter the resulting file name")
    window.geometry("400x200")
    newFileStringVar = tk.StringVar()
    newFileEntry = tk.Entry(window, textvariable=newFileStringVar)
    newFileEntry.pack()
    button = tk.Button(window, text="Enter", command=lambda: newAudioFile(audio, filePath, newFileStringVar, window))
    button.pack()
    window.mainloop()

def updateFilePath():
    filePath = fileEntry.get().replace('"', '')
    if os.path.exists(filePath):
        audio = AudioSegment.from_mp3(filePath)
        fileInputWindow(audio, filePath)
        messagebox.showinfo(title="Success", message="The worsened file is in the same directory as the original!")
    else:
        messagebox.showerror(title="Error", message="Ivalid file/directory")

lbl = tk.Label(root, text = "Enter the file path (and name) (must be an mp3): ")
lbl.pack()

fileEntry = tk.StringVar()
text = tk.Entry(root, textvariable=fileEntry)
text.pack()

button = tk.Button(root, text="Enter", command=updateFilePath)
button.pack()

root.mainloop()