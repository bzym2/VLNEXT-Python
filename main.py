from tkinter import messagebox
from win32mica import ApplyMica
from win32gui import GetParent
import ttkbootstrap as tk
import tkinter as tk2
import subprocess
import BlurWindow
import globalvars
import os
import easygui
hWnd = 0
def Get_hWnd():
    global hWnd
    hWnd = GetParent(root.winfo_id())
    if(globalvars.window_mode=="Black"):
        pass
    elif(globalvars.window_mode=="Mica"):
        ApplyMica(hWnd)
y1=100
def initalize():
    global root,label,button
    root = tk2.Tk()
    root.title("VirtualLauncher NEXT")
    root.geometry("600x350")
    root.iconbitmap(None)
    root.resizable(False, False)
    label = tk.Label(root, text="VirtualLauncher NEXT", foreground="#FFFFFF", background="#000000", font=("MontserratAlt1-SemiBold.ttf", 20))
    label.place(x=140, y=y1)
    button = tk.Button(root, text="下一步", command=launch)
    button.place(x=140,y=200)
    root.configure(bg="#000000")
    root.after(1, Get_hWnd)
    root.mainloop()
    return
def launch():
    global label
    label.config(text="正在从 Github 下载核心")
    globalvars.run_core(["certutil","-urlcache","-split","-f","https://gitdl.cn/https://github.com/MrShieh-X/console-minecraft-launcher/releases/latest/download/cmcl.exe","core.exe"])
    root.destory()
    main()
    return

def debug():
    globalvars.run_core(easygui.enterbox("请输入要执行的命令", "VLN Debug Demo").split(" "))
def main():
    global root
    root = tk2.Tk()
    root.title("VirtualLauncher NEXT")
    root.geometry("600x350")
    root.iconbitmap(None)
    root.resizable(False, False)
    label = tk.Label(root, text="VLN Debug Demo", foreground="#FFFFFF", background="#000000", font=("MontserratAlt1-SemiBold.ttf", 20))
    label.place(x=140, y=y1)
    button = tk.Button(root, text="执行", command=debug)
    button.place(x=140,y=200)
    root.configure(bg="#000000")
    root.after(1, Get_hWnd)
    root.mainloop()
    return

if(os.path.exists("core.exe")):
    main()
else:
    initalize()

