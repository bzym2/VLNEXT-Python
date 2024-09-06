import platform
import os
import requests
import subprocess
import threading
import tkinter as tk
import ttkbootstrap
from ttkbootstrap import Style
from ttkbootstrap.constants import *
winnt = platform.release()
sys = platform.system()
envpath = os.environ['PATH']
window_mode = "Mica"
def download(url:str,fname:str):
    resp = requests.get(url, stream=True)
    total = int(resp.headers.get('content-length', 0))
    with open(fname, 'wb') as file, tqdm(
        desc=fname,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)


def run_core(command):
    def create_gui(command):
        global root
        root = tk.Tk()
        root.title("核心运行结果")
        root.resizable(0,0)

        # 创建文本框
        text_box = ttkbootstrap.Text(root, wrap=tk.WORD, height=20, width=80)
        text_box.pack(padx=10, pady=10)

        # 创建滚动条
        scrollbar = ttkbootstrap.Scrollbar(root, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_box.config(yscrollcommand=scrollbar.set)

        # 运行命令
        run_command_in_thread(command, text_box)
        root.mainloop()
    def update_output(text_box, process):
        for line in iter(process.stdout.readline, ''):
            text_box.insert(tk.END, line)
            text_box.see(tk.END)

        process.wait()
        if process.returncode == 0:
            root.after_idle(root.destroy)
        else:
            text_box.insert(tk.END, f"\nCommand exited with code {process.returncode}\n")
            text_box.see(tk.END)

    def run_command_in_thread(command, text_box):
        startupinfo = None
        if os.name == 'nt':
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            startupinfo=startupinfo
        )

        thread = threading.Thread(target=update_output, args=(text_box, process))
        thread.start()


    create_gui(command)