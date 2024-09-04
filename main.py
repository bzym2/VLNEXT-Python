from tkinter import ttk,messagebox
from win32mica import ApplyMica
from win32gui import GetParent
import ttkbootstrap as tk
import tkinter as tk2
import os
import platform
import globalvars
hWnd = 0
mica_enabled = True
def getWindowsNTVersion():
    return platform.release()
def Get_hWnd():
    global hWnd
    hWnd = GetParent(root.winfo_id())
    ApplyMica(hWnd)
def initalize():
    global root
    root = tk2.Tk()
    root.title("VirtualLauncher NEXT")
    root.geometry("600x300")
    #隐藏窗口图标
    root.iconbitmap(None)
    root.resizable(False, False)
    label = tk.Label(root, text="VirtualLauncher NEXT", foreground="#FFFFFF", background="#000000", font=("MontserratAlt1-SemiBold.ttf", 20))
    label.place(x=140, y=100)
    # button = tk.Button(root, text="Launch", command=launch)
    # button.pack()
    root.configure(bg="#000000")
    root.after(1, Get_hWnd)
    root.mainloop()
    return
def launch():
    os.system("start cmd /k echo 未完成")
    return
initalize()
messagebox.showinfo("Debug",f"OS_VERSION:{getWindowsNTVersion()}")