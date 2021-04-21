#!/usr/bin/python
import tkinter as tk
from time import sleep

STAGES = [
    'Running updater',      # Open the updater (if the text does not show something is wrong)
    'Reading parameters',   # Use the updater parameters
    'Fetching repository',  # Seek for the repository
    'Downloading update',   # Download the latest release
    'Unpacking update',     # Unzip the latest release
    'Cleaning',             # Delete the zip file
    'Closing updater'       # Close the updater (if the text shows something might be wrong)
]

class GUI(tk.Frame):
    def __init__(self, master=None, width:int=192, height:int=108):
        super().__init__(master)
        self.master = master
        self.pack(side='top', expand=1)
        self.master.minsize(width, height)
        self.master.maxsize(960, 540)
        self.create_widgets()
    
    def create_widgets(self):
        self.running_text = tk.Label(text='Running updater...')
        self.running_text.pack(side='top')
    
    def update_widgets(self, stage:int=0):
        self.running_text['text'] = f"{STAGES[stage]}..."
            

if __name__ == '__main__':
    root = tk.Tk()
    app = GUI(master=root)

    for i in range(len(STAGES)):
        app.update_widgets(i)
        sleep(1)
        app.update_idletasks()
    
    root.destroy()
