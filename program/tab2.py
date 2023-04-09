from win10toast_click import ToastNotifier
import threading
import time
import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import *
from win10toast_click import ToastNotifier


def filltab2(tab2):
    tab2canvas = tk.Canvas(tab2, width=600, height=300)
    tab2canvas.grid(columnspan=3, rowspan=3)
    # Buttons
    example_text = tk.StringVar()
    example_btn = tk.Button(tab2, textvariable=example_text, command=lambda: open_body_healthcare_notif(),
                            font="Raleway",
                            bg="#20bebe",
                            fg="white",
                            height=2,
                            width=10)
    example_text.set("Пример\nуведомления")
    example_btn.grid(column=0, row=0)
    tab2canvas.create_text(480, 20, text="ඞ", fill="black")
    return
