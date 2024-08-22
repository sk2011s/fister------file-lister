import format_handler
from subprocess import getstatusoutput
from colorama import Fore
from os import _exit


def run(path, list_path):
    #path = filedialog.askdirectory()
    #list_path = filedialog.askdirectory()

    with open("formats.txt") as file:
        formats = file.readlines()
    
    print(Fore.YELLOW + " listing your files...]" + Fore.WHITE)
    
    try:
        files = getstatusoutput(f'dir /b "{path}"')
    except:
        
        print(Fore.RED + ' faild to load files' + Fore.WHITE)
        
        _exit()
    
    print(Fore.WHITE + str(files))
    
    print(Fore.GREEN + " listing files complete!" + Fore.WHITE)
    
    print(Fore.YELLOW + " making folders..." + Fore.WHITE)
    

    print(rf"{list_path}")

    #for formatn in formats:
    #    folder_name = os.path.join((rf"{list_path}"), str(formatn.replace("\n", "")))
    #    os.makedirs(folder_name, exist_ok=True)
    #    print(f"{str(formatn.replace("\n", ""))} was created")
    try:
        format_handler.create_folders(formats, list_path=list_path)
    except:
        
        print(Fore.RED + ' faild to make folders' + Fore.WHITE)
        
        _exit()
    
    print(Fore.GREEN + " folder making complete!" + Fore.WHITE)
    
    print(Fore.YELLOW + " making shortcuts..." + Fore.WHITE)
    
    try:
        format_handler.listBy_formats(files=files, list=formats, list_path=list_path)
    except:
        
        print(Fore.RED + ' faild to make shortcuts' + Fore.WHITE)
        
        _exit()
    
    print(Fore.GREEN + " making shortcuts complete!" + Fore.WHITE)
    
    print(Fore.GREEN + ' \n\n complete!' + Fore.WHITE)
    

