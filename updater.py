# Import included libraries
import urllib.request as dlurl
from os import path
from json import loads
from zipfile import ZipFile

# Parameters
auto_update = True
auto_download = False
github_user = 'Vianpyro'
github_repo = 'Python-Updater'

source_website = 'https://api.github.com'

# Updater parameters (Don't change this if you want to be aware of published updates)
updater_auto_update = True
updater_auto_download = False
updater_user = 'Vianpyro'
updater_repo = 'Python-Updater'

parameters = [
    [auto_update, auto_download, github_user, github_repo],
    [updater_auto_update, updater_auto_download, updater_user, updater_repo]
]

for i in range(len(parameters)):
    if parameters[i][0]:
        try:
            resp = dlurl.urlopen(
                f'{source_website}/repos/{parameters[i][2]}/{parameters[i][3]}/releases/latest'
            )
            data = loads(resp.read())
            version = data['html_url'].split('/')[-1]

            if parameters[i][1]:
                if path.exists(f'{version}.zip'):
                    print(f'Your program is already running on the most recent version: {version}!')
                else:
                    if __name__ == "__main__":
                        print(f'Downloading {version}...')
                        dlurl.urlretrieve(
                            f'{source_website}/{parameters[i][2]}/{parameters[i][3]}/archive/{version}.zip',
                            f'{version}.zip'
                        )
                        print(f'Downloaded {version} successfully.')
                    
                    if not path.exists(f'{github_repo}-{version[1:]}'):
                        print(f'Extracting {version}...')
                        with ZipFile(f'{version}.zip', 'r') as zipf:
                            zipf.extractall()
                            zipf.close()
                            print(f'Extracted {version} successfully.')
            else:
                print(
                    f'A new version of this program may be available: {version}, use the updater to download the latest version!'
                )
        except: 
            print(
                f'Unable to locate package: "{source_website}/repos/{parameters[i][2]}/{parameters[i][3]}/releases/latest"...'
            )
    if updater_user == github_user and updater_repo == github_repo:
        quit()