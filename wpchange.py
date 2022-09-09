import datetime
import ctypes
import time
import os
from tkinter import filedialog
from tkinter import *


location=''
def changewallpaper(file):
    today = datetime.datetime.now()
    date_time = today.strftime("%H")
    if(int(date_time)<10):
    	date_time=int(date_time)%10
    path = file +"\\"+str(date_time)+'.jpg'
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
    print("wallpaper set sucesfully")

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
    

# s=input(" Do you want to select foler (y/n) \n ")
s='n'
if(s=="y"):
    select_folder()
    prev_path()
else:
    print_path()
