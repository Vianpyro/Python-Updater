#!/usr/bin/python
from os import path, remove
from zipfile import ZipFile
import json
import requests
import tkinter as tk
import urllib.request as dlurl

# Parameters
source_website = 'https://api.github.com'
auto_download = True
github_user = 'Vianpyro'
github_repo = 'python_updater'


class GUI(tk.Frame):
    def __init__(self, master=None, width:int=192, height:int=108):
        super().__init__(master)
        self.master = master
        self.pack(side='top', expand=1)
        self.master.minsize(width, height)
        self.master.maxsize(960, 540)
        self.create_widgets()
        self.update()
    
    def create_widgets(self):
        self.running_text = tk.Label(text='Running updater...')
        self.running_text.pack(side='top')
    
    def update(self):
        self.stages = [
            'Running updater',      # Open the updater (if the text does not show something is wrong)
            'Reading parameters',   # Use the updater parameters
            'Fetching repository',  # Seek for the repository
            'Downloading update',   # Download the latest release
            'Unpacking update',     # Unzip the latest release
            'Cleaning',             # Delete the zip file
            'Closing updater'       # Close the updater (if the text shows something might be wrong)
        ]

        for i in range(len(self.stages)):
            self.running_text['text'] = f"{self.stages[i]}..."
            self.update_idletasks()
            stage_name = self.stages[i].lower()

            if 'parameter' in stage_name:
                # Reading parameters
                self.source = source_website
                self.download = auto_download
                self.user = github_user
                self.repo = github_repo
            elif 'fetch' in stage_name:
                # Fetch the latest release
                self.repo_json = requests.get(f'{self.source}/repos/{self.user}/{self.repo}/releases').json()
                self.latest_release_tag = self.repo_json[0]['tag_name']
            elif 'download' in stage_name:
                # Download the latest release
                dlurl.urlretrieve(
                    f'https://github.com/{self.user}/{self.repo}/archive/{self.latest_release_tag}.zip',
                    f'{self.repo}_{self.latest_release_tag}.zip'
                )
            elif 'unpack' in stage_name:
                # Unzipping the latest release
                with ZipFile(f'{self.repo}_{self.latest_release_tag}.zip', 'r') as zipf:
                    zipf.extractall()
                    zipf.close()
            elif 'clean' in stage_name:
                remove(f'{self.repo}_{self.latest_release_tag}.zip')


if __name__ == '__main__':
    root = tk.Tk()
    app = GUI(master=root)
    root.destroy()
