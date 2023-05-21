from win10toast_click import ToastNotifier
import threading
import time
import webbrowser
from program.func import *
import tkinter as tk
from tkinter import ttk
from tkinter import *
from win10toast_click import ToastNotifier
from PIL import ImageTk, Image


def filltab2(tab2):
    tab2canvas = tk.Canvas(tab2, width=600, height=300)
    tab2canvas.configure(bg='#C3E8BD')
    tab2canvas.grid(columnspan=3, rowspan=4)
    # Buttons
    start_btn = tk.Button(tab2, text="Старт",
                          font="Bahnschrift",
                          bg="#2e5339",
                          fg="#C3E8BD",
                          height=1,
                          width=7)
    start_btn.grid(column=1, row=0)
    pause_btn = tk.Button(tab2, text="Пауза",
                          font="Bahnschrift",
                          bg="#2e5339",
                          fg="#C3E8BD",
                          height=1,
                          width=7)
    pause_btn.grid(column=2, row=0)
    stop_btn = tk.Button(tab2, text="Стоп",     font="Bahnschrift",   bg="#2e5339", fg="#C3E8BD",height=1, width=7)
    stop_btn.grid(column=0, row=3)

    heading_lbl = ttk.Label(tab2, text="Помидорковый таймер", style="Text.TLabel")
    heading_lbl.grid(column=1, row=0, sticky="n", pady="10")
    return


def filltab3(tab3):
    tab2canvas = tk.Canvas(tab3, width=600, height=300)
    tab2canvas.grid(columnspan=4, rowspan=2)
    tab2canvas.configure(bg='#C3E8BD')
    stick_img = ImageTk.PhotoImage(Image.open("sticker.jpg"))
    label = Label(tab3, image=stick_img)
    label.image = stick_img
    label.grid(row=0, columnspan=6)
