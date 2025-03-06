# Audio Distorter
This program takes in a path to a file and saves a new file with worse audio quality (more specifically, it uses ffmpeg to output a new file at a 4 kilobit bitrate).
To use it, enter the path of the file, and then enter the name of the destination file.

## Prerequisites
### ffmpeg
https://ffmpeg.org/download.html
Select the download appropriate for your operating system.
### Python 3.13
Other versions probably work but this was built and tested on Python 3.13.

#### Libraries Used
see [here](requirements.txt)

# WIP
- Support for a simple install with included libraries
- Prettier interface
- Fixing tkinter so that the final success message displays before the main window closes
