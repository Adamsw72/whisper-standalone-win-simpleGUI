import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkinter import Entry, Button, StringVar, Label, ttk, messagebox, StringVar
from pytube import YouTube
import os
from threading import Thread
from urllib.request import urlretrieve
import subprocess
import time
from customtkinter import *

# Get the directory where the script or executable is located
if getattr(sys, 'frozen', False):
    # Running as compiled
    base_path = os.path.dirname(sys.executable)
else:
    # Running as a script
    base_path = os.path.abspath(os.path.dirname(sys.argv[0]))

# Set the working directory to the directory of the script or executable
os.chdir(base_path)

# Dynamic working directory
working_directory = {base_path}

# Default download directory
default_download_directory = os.path.join(os.path.expanduser("~"), "Downloads")

# Global variable to store the downloaded file path
file_path = None
downloaded_file_path = None


def on_drop(event):
    global file_path
    file_path = event.data
    # Remove curly braces if present
    file_path = file_path.strip('{}')
    print(f"File dropped: {file_path}")

    file_path = os.path.abspath(file_path)

    # Invoke the CMD command for dropped file
    process_dropped_file()

def process_dropped_file():
    global selected_model, selected_task, selected_language
    selected_model = menu_model.get()  # Get the current value from the dropdown menu
    selected_task = menu_task.get()
    selected_language = menu_language.get()
    print(selected_model, selected_task, selected_language)
    
    global file_path

    # Hide the Tkinter window
    root.iconify()

    working_directory = {base_path}
    print(f"Changed working directory to: {base_path}")

    # Example CMD command: Use the file path in a CMD command
    cmd_command = f'whisper-faster "{file_path}" --language {selected_language} --task {selected_task} --model {selected_model}'
    
    #use this to debug the command
    #print(f"CMD command: {cmd_command}")
    subprocess.run(cmd_command, shell=True)
    
    # Withdraw the Tkinter window
    root.iconify()
    root.after(100, lambda: root.destroy())  # Destroy the window after a short delay (100 milliseconds)

    # Example CMD command: Display the file path in CMD
    cmd_command = f'echo The selected file path is: {file_path}'
    subprocess.run(cmd_command, shell=True)

def download_video():
    try:
        # Create a YouTube object
        yt = YouTube(url_entry.get())

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Set up progress bar and labels
        progress_var.set(0)
        total_size = video_stream.filesize
        file_size_var.set(f"File Size: {total_size / (1024 * 1024):.2f} MB")
        speed_var.set("Download Speed: Calculating...")

        progress_bar["maximum"] = 100

        # Download the video in a separate thread
        download_thread = Thread(target=download_in_thread, args=(video_stream, total_size, yt.title))
        download_thread.start()

    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

def download_in_thread(video_stream, total_size, video_title):
    try:
        # Create a valid file name by removing invalid characters
        video_title = "".join([c for c in video_title if c.isalnum() or c in [' ', '-', '_']]).rstrip()

        output_path = os.path.join(default_download_directory, f"{video_title}.mp4")
        url = video_stream.url

        def download_callback(count, block_size, total_size=total_size):
            downloaded_size = count * block_size
            progress = (downloaded_size / total_size) * 100
            progress_var.set(progress)

            file_size_var.set(f"File Size: {downloaded_size / (1024 * 1024):.2f} MB / {total_size / (1024 * 1024):.2f} MB")

            elapsed_time = time.time() - start_time
            if elapsed_time > 0:
                speed = (downloaded_size / 1024) / elapsed_time
                speed_var.set(f"Download Speed: {speed:.2f} KB/s")

        # Download the video using urlretrieve
        start_time = time.time()
        urlretrieve(url, output_path,
                    lambda count, block_size, total_size=total_size: download_callback(count, block_size, total_size))

        progress_var.set(100)
        speed_var.set("Download Speed: Completed")
        
        # Hide the Tkinter window
        root.iconify()
        
        global file_path
        file_path = output_path
        
        # Process the downloaded file
        process_dropped_file()
        

    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")
        

# Initialize Tkinter window
root = TkinterDnD.Tk()
root.title("faster-whisper : Simple GUI")
root.resizable(False, False)

class CBtkToolTip(object):
    def __init__(self, widget, text='widget info', bg_color=None, fg_color=None):
        self._bg_colour = '#000000' if bg_color is None else bg_color  # black background
        self._fg_color = '#ffffff' if fg_color is None else fg_color  # white font
        self._wait_time = 400  # milli-seconds
        self._wrap_length = 300  # pixels
        self._widget = widget
        self._text = text
        self._widget.bind("<Enter>", self.on_enter)
        self._widget.bind("<Leave>", self.on_leave)
        self._widget.bind("<ButtonPress>", self.on_leave)
        self._id = None
        self._tw = None

    def on_enter(self, event=None):
        self._schedule()

    def on_leave(self, event=None):
        self._unschedule()
        self.hide_tooltip()

    def _schedule(self):
        self._unschedule()
        self._id = self._widget.after(self._wait_time, self.show_tooltip)

    def _unschedule(self):
        id = self._id
        self._id = None
        if id:
            self._widget.after_cancel(id)

    def show_tooltip(self, event=None):
        x = y = 0
        x, y, cx, cy = self._widget.bbox("insert")
        x += self._widget.winfo_rootx() + 40
        y += self._widget.winfo_rooty() + 20
        self._tw = tk.Toplevel(self._widget)
        self._tw.wm_overrideredirect(True)
        self._tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self._tw, text=self._text, justify='left', fg=self._fg_color,
                         bg=self._bg_colour, relief='solid', borderwidth=1,
                         wraplength=self._wrap_length)
        label.pack(ipadx=1)

    def hide_tooltip(self):
        tw = self._tw
        self._tw = None
        if tw:
            tw.destroy()

#    Drop Menu

def on_model_selected(event):
    global selected_model
    selected_model = menu_model.get()
    #print("Using model:", selected_model)

def on_task_selected(event):
    global selected_task
    selected_task = menu_task.get()
    #print("Selected Task:", selected_task)

def on_language_selected(event):
    global selected_language
    selected_language = menu_language.get()
    #print("Selected Language:", selected_language)

label_model = Label(root, text="AI Model:")
label_model.pack(pady=10)
label_task = Label(root, text="          Task:", justify= 'center')
label_task.place(x=10, y=9)
label_language = Label(root, text="        Language:", justify= 'center')
label_language.place(x=290, y=9)


selected_model = StringVar(value="large-v3")
menu_model = CTkComboBox(root, justify= "center", values=["large-v3", "medium"], command = on_model_selected, variable=selected_model, width=100)
tooltip_model = CBtkToolTip(menu_model, text='Select the AI model')
menu_model.pack()

selected_task = StringVar(value="transcribe")
menu_task = CTkComboBox(root, justify= "center", values=["transcribe", "translate"], command = on_task_selected, variable=selected_task, width=100)
tooltip_task = CBtkToolTip(menu_task, text='Transcribe : whether to perform X to X speech recognition\nTranslate : X to English translation')
menu_task.place(x=10, y=41)

selected_language = StringVar(value="en")
menu_language = CTkComboBox(root, justify= "center", values=["en", "id", "ja"], command = on_language_selected, variable=selected_language, width=100)
tooltip_language = CBtkToolTip(menu_language, text='Select the output language\n\nen=english\nid=indonesia\nja=japanese\n\nor if the languages are not available on this dropdown menu just type any languages that available on whisper-standalone-win ')
menu_language.place(x=290,y=41)


menu_model.bind("<<ComboboxSelected>>", lambda event: on_model_selected(event))
menu_task.bind("<<ComboboxSelected>>", lambda event: on_task_selected(event))
menu_language.bind("<<ComboboxSelected>>", lambda event: on_language_selected(event))


# Set the window icon using a Tcl/Tk command
icon_path = 'F://Artificial-Intelligence//faster-whisper-0.10.0//icon.ico'  # Replace with your ICO file path
if os.path.isfile(icon_path):
    root.tk.call('wm', 'iconbitmap', root._w, icon_path)

# Configure the window to accept drops
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', on_drop)

#output_directory = 'F:\Download\Video'  # Set your output directory here

# Create a label for instructions
instructions_label = tk.Label(root, text="Drag and drop a file into this window\nor\nDownload from YouTube by pasting the link below.")
instructions_label.pack(pady=10)

# Create an Entry widget for the YouTube link
url_entry = CTkEntry(root, placeholder_text="Paste URL here...", width=250)
url_entry.pack(pady=10)

# Create a Button to initiate the download
download_button = CTkButton(root, text="Download Video" , command=download_video)
download_button.pack(pady=10)

# Create a progress bar
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, length=300, maximum=100)
progress_bar.pack(pady=10)

# Create labels for file size and download speed
file_size_var = StringVar()
file_size_label = Label(root, textvariable=file_size_var)
file_size_label.pack(pady=5)

speed_var = StringVar()
speed_label = Label(root, textvariable=speed_var)
speed_label.pack(pady=5)

# Set the window size
root.geometry("400x350")

# Run the Tkinter event loop
root.mainloop()
