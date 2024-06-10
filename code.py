from tkinter import *
from pytube import YouTube
import threading

# Function to download the video
def download_video():
    url = t1.get()  # Get the URL from the entry widget
    l2.config(text="Downloading", fg="blue")  # Update the status label
    try:
        link = YouTube(url)
        # video = link.streams.get_highest_resolution()
        # video = link.streams. filter(only_audio=True).first()
        video = link.streams.first()
        video.download()  # Download the video
        l2.config(text="Download Complete", fg="green")  # Update the status label
    except Exception as e:
        l2.config(text="Error: " + str(e), fg="red")  # Update the status label in case of error

# Function to run the download in a separate thread
def start_download():
    threading.Thread(target=download_video).start()

# Create the main window
dsp = Tk()
dsp.geometry("500x200")
dsp.title("YouTube Video Downloader")

# Create and place the widgets
l1 = Label(dsp, text="Enter the URL")
l1.pack(pady=10)

t1 = Entry(dsp, width=50)
t1.pack(pady=10)

b1 = Button(dsp, text="Download Now", command=start_download)
b1.pack(pady=10)

l2 = Label(dsp, text="")
l2.pack(pady=10)

# Start the Tkinter event loop
dsp.mainloop()
