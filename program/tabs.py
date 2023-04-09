from win10toast_click import ToastNotifier
import threading
import time
import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import *
from win10toast_click import ToastNotifier
from PIL import ImageTk, Image


def filltab2(tab2):
    tab2canvas = tk.Canvas(tab2, width=600, height=300)
    tab2canvas.grid(columnspan=3, rowspan=3)
    # Buttons
    example_text = tk.StringVar()
    example_btn = tk.Button(tab2, textvariable=example_text,
                            font="Raleway",
                            bg="#20bebe",
                            fg="white",
                            height=2,
                            width=10)
    example_text.set("Пример\nуведомления")
    example_btn.grid(column=0, row=0)
    tab2canvas.create_text(480, 20, text="ඞ", fill="black")
    return


def filltab3(tab3):
    tab2canvas = tk.Canvas(tab3, width=600, height=300)
    tab2canvas.grid(columnspan=4, rowspan=2)

    stick_img = ImageTk.PhotoImage(Image.open("sticker.jpg"))
    label = Label(tab3, image=stick_img)
    label.image = stick_img
    label.grid(row=0, columnspan=6)
