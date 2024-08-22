import tkinter as tk
from tkinter import filedialog
import sort

global path, list_path
path = ''
list_path = ''

def Browse_Directory():
    global path, list_path
    path = filedialog.askdirectory()
    dir.insert(0,path)
    
def Browse_ListDirectory():
    global path, list_path
    list_path = filedialog.askdirectory()
    listdir.insert(0,list_path)

def run():
    global path, list_path 
    if path != '' and list_path != '':
        sort.run(path=path, list_path=list_path)
        root.destroy()

root = tk.Tk()
root.title('file sorter')

dir = tk.Entry(root)
dir.pack()
directory = tk.Button(root, text='Browse Directory', command=Browse_Directory).pack()
listdir = tk.Entry(root)
listdir.pack()
list_directory = tk.Button(root, text='Browse List Directory', command=Browse_ListDirectory).pack()


submit = tk.Button(root, text='Submit', command=run)
submit.pack()



root.mainloop()