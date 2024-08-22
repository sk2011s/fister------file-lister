from pyshortcuts import make_shortcut
from os.path import basename


def make(file_path, shortcut_folder):
    #file_path = r"C:\Windows\System32\cmd.exe"
    # مسیر فایل اصلی
    target_path = file_path
    
    # ایجاد شورتکات
    print(file_path)
    make_shortcut(file_path, folder=shortcut_folder, name=basename(target_path), icon=str((file_path, 0)))

