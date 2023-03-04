import datetime
import ctypes
import time
import msvcrt
import os
from tkinter import filedialog
from tkinter import *


location=''
def changewallpaper(filepath):
    today = datetime.datetime.now()
    date_time = int(today.strftime("%H"))
    if date_time < 10:
        date_time %= 10
    imgpath = os.path.join(filepath, f"{date_time}.jpg")
    if os.path.exists(imgpath):
        try:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, imgpath, 0)
            print("Wallpaper set successfully")
        except:
            print("Error setting wallpaper")
    else:
        print(f"Image not found: {imgpath}")

def select_folder():
    global location
    root = Tk()
    root.withdraw()
    file = filedialog.askdirectory()
    
    for i in file:
        if(i=='/'):
            location = location+"\\"
        else:
            location = location+i
    changewallpaper(location)

def prev_path():
    global location
    file1 = open("path.txt","w")
    file1.write(location)
    file1.close()
def print_path():
    file1 = open("path.txt","r+") 
    x=file1.read()
    changewallpaper(x)
    # print(x)
    file1.close()
    




timeout = 3
start_time = time.time()

while True:
    if msvcrt.kbhit():
        key = msvcrt.getch()

        if key == b'y':
            # print("y")
            select_folder()
            prev_path()
            break
        else:
            # print("n")
            print_path()
            break

    elapsed_time = time.time() - start_time
    if elapsed_time >= timeout:
        print("Timed out, using default value of 'n'")
        print_path()
        break




# print("Stopped typing")
