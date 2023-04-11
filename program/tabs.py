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
    tab2canvas.grid(columnspan=3, rowspan=3)
    # Buttons
    example_text = tk.StringVar()
    example_btn = tk.Button(tab2, textvariable=example_text,
                            font="Raleway",
                            bg="#2e5339",
                            fg="#C3E8BD",
                            height=2,
                            width=10)
    example_text.set("Включить\nтаймер")
    example_btn.grid(column=1, row=2)
    tab2canvas.create_text(300, 20, text="Уход за глазами это очень важно и многие об этом забывают, \nмы предлагаем Вам попробовать поработать в формате '25 минут работы / 5 минут отдыха'", fill="black")
    tab2canvas.create_text(300, 40, text="Включив таймер, пойдет отсчет 25 минут, затем вам высветится напоминание, что стоит сделать перерыв", fill="black")
    tab2canvas.create_text(300, 50,
                           text="Вы можете сделать предложенную нами зарядку для глаз или просто насладиться видом за окном",
                           fill="black")
    tab2canvas.create_text(300, 80,
                           text="здесь может быть анимация (просто украденная или Полина нарисует) с простой зарядочкой",
                           fill="black")
    return


def filltab3(tab3):
    tab2canvas = tk.Canvas(tab3, width=600, height=300)
    tab2canvas.grid(columnspan=4, rowspan=2)
    tab2canvas.configure(bg='#C3E8BD')
    stick_img = ImageTk.PhotoImage(Image.open("sticker.jpg"))
    label = Label(tab3, image=stick_img)
    label.image = stick_img
    label.grid(row=0, columnspan=6)
