from os import path, makedirs
from make_short import make
from colorama import Fore

def create_folders(list, list_path):
    for formatn in list:
        folder_name = path.join((rf"{list_path}"), str(formatn.replace("\n", "")))
        makedirs(folder_name, exist_ok=True)
        
        print(Fore.WHITE + f" {str(formatn.replace("\n", "")).replace('.', '')} was created")

def listBy_formats(files, list, list_path):
    files = files[1].split('\n')
    for file in files:
        for format in list:
           # print(file.endswith(f'.{format.replace('\n', '')}'))
            if file.endswith(f'.{format.replace('\n', '')}'):
                
                print(Fore.WHITE + ' ' + file)
                make(file_path=file, shortcut_folder=rf'{list_path.replace('\n','')}\{format.replace('\n','')}')
