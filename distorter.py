import os
from pydub import AudioSegment
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd

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
    window.destroy()
    messagebox.showinfo(title="Success", message="file saved as " + fileDir + "/" + newFileName)

def fileInputWindow(audio: AudioSegment, filePath: str):
    window = tk.Toplevel(root)
    window.title("Enter the resulting file name")
    window.geometry("400x200")
    newFileStringVar = tk.StringVar()
    newFileEntry = tk.Entry(window, textvariable=newFileStringVar)
    newFileEntry.pack()
    button = tk.Button(window, text="Enter", command=lambda: newAudioFile(audio, filePath, newFileStringVar, window))
    button.pack()

def selectFile():
    fileTypes = [('MP3 Files', 'mp3')]
    fileName = fd.askopenfilename(
        title = 'Open a file',
        initialdir = os.path.expanduser('~'),
        filetypes = fileTypes
    )
    if not fileName:
        return None
    else:
        return str(fileName)

def updateFilePath():
    selected = selectFile()
    if not selected:
        return
    filePath = os.path.expanduser(selected.replace('"', ''))
    if os.path.exists(filePath):
        audio = AudioSegment.from_mp3(filePath)
        fileInputWindow(audio, filePath)
    else:
        messagebox.showerror(title="Error", message="Ivalid file/directory")

lbl = tk.Label(root, text = "Select an mp3 file to distort:")
lbl.pack()

openButton = tk.Button(root, text='Browse Files', command=updateFilePath)
openButton.pack()

root.mainloop()