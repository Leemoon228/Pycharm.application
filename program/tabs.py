import concurrent.futures

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
import sqlite3
import re


def validate(new_val):
    return re.match("^\d{0,2}\:[012345]?[0123456789]?$", new_val) is not None


def timer_start(duration_entry, sleep_entry, timer):
    minutes, seconds = int(duration_entry.get()[0:2]), int(duration_entry.get()[2:])
    duration_entry.config(state="disabled")
    sleep_entry.config(state="disabled")
    timer.daemon = True
def label_change():
    counter = 0







def filltab2(tab2):
    tab2canvas = tk.Canvas(tab2, width=600, height=300)
    tab2canvas.configure(bg='#C3E8BD')
    tab2canvas.grid(columnspan=3, rowspan=4)
    check = (tab2.register(validate), "%P")

    heading_lbl = ttk.Label(tab2, text="Помидорковый таймер", style="Text.TLabel")
    heading_lbl.grid(column=1, row=0, sticky="n", pady="2")

    TimeDuration_lbl = ttk.Label(tab2, text="Длительность \nработы", style="Text.TLabel")
    TimeDuration_lbl.grid(column=0, row=0, sticky="nw", pady="65")
    TimeDuration_entry = tk.Entry(tab2, validate="key", validatecommand=check, width=5,
                                  font=("Bahnschrift", 15), background="#C3E8BD", justify="center",
                                  selectborderwidth="0")
    TimeDuration_entry.insert(0, "30:00")
    TimeDuration_entry.grid(column=0, row=0, rowspan=2, sticky="nw", pady="105", padx="16")

    TimeBreak_lbl = ttk.Label(tab2, text="Длительность \nперерыва", style="Text.TLabel")
    TimeBreak_lbl.grid(column=0, row=0, rowspan=2, sticky="sw", pady="50")
    TimeSleeping_entry = tk.Entry(tab2, validate="key", validatecommand=check, width=5,
                                  font=("Bahnschrift", 15), background="#C3E8BD", justify="center",
                                  selectborderwidth="0")
    TimeSleeping_entry.insert(0, "5:00")
    TimeSleeping_entry.grid(column=0, row=0, rowspan=2, sticky="sw", pady="20", padx="16")

    CurrentTimer_lbl = ttk.Label(tab2, text="Работа", style="Text.TLabel", justify="center")
    CurrentTimer_lbl.grid(column=1, columnspan=2, row=0, pady="30", padx="175", sticky="ne")

    CurrentTimerTime_lbl = ttk.Label(tab2, text="30:00", style="Text.TLabel", font=("Bahnschrift", 18),
                                     justify="center")
    CurrentTimerTime_lbl.grid(column=1, columnspan=2, row=0, pady="50", padx="175", sticky="ne")

    image_height, image_width = 95, 100
    tomato_img = ImageTk.PhotoImage(
        Image.open("fingtomato.png").resize((image_width + 4, image_height + 4), Image.ANTIALIAS))

    tomato1_lbl = Label(tab2, image=tomato_img, width=image_width, height=image_height)
    tomato1_lbl.image = tomato_img
    tomato1_lbl.grid(column=1, row=1, rowspan=3, sticky="ne", padx=70)

    tomato2_lbl = Label(tab2, image=tomato_img, width=image_width, height=image_height)
    tomato2_lbl.image = tomato_img
    tomato2_lbl.grid(column=2, row=1, rowspan=3, sticky="ne", padx=30)

    tomato3_lbl = Label(tab2, image=tomato_img, width=image_width, height=image_height)
    tomato3_lbl.image = tomato_img
    tomato3_lbl.grid(column=1, row=0, sticky="se", pady=20, padx=70)

    tomato4_lbl = Label(tab2, image=tomato_img, width=image_width, height=image_height)
    tomato4_lbl.image = tomato_img
    tomato4_lbl.grid(column=2, row=0, sticky="se", pady=20, padx=30)

    Timer = threading.Timer(1, label_change, args=[CurrentTimer_lbl, CurrentTimerTime_lbl])

    # Buttons
    start_btn = tk.Button(tab2, text="Старт",
                          font="Bahnschrift",
                          bg="#2e5339",
                          fg="#C3E8BD",
                          height=1,
                          width=7, command=lambda: timer_start(TimeDuration_entry, TimeSleeping_entry, Timer))
    start_btn.grid(column=1, row=0, sticky="n", pady="30")
    pause_btn = tk.Button(tab2, text="Пауза",
                          font="Bahnschrift",
                          bg="#2e5339",
                          fg="#C3E8BD",
                          height=1,
                          width=7)
    pause_btn.grid(column=2, row=0, sticky="n", pady="30")

    stop_btn = tk.Button(tab2, text="Стоп", font="Bahnschrift", bg="#2e5339", fg="#C3E8BD", height=1, width=7)
    stop_btn.grid(column=0, row=3, sticky="sw", pady="10", padx="30")

    return


def filltab3(tab3):
    conn = sqlite3.connect('tasks.db')
    tab2canvas = tk.Canvas(tab3, width=600, height=300)
    rowspan = conn.execute('SELECT COUNT(ROWID) FROM TASKS')
    tab2canvas.grid(columnspan=3, rowspan=rowspan.fetchone()[0] + 2)
    Label(tab3, text="Название").grid(row=0, column=0)
    Label(tab3, text="Истекает до").grid(row=0, column=1)
    Label(tab3, text="Уведомлять").grid(row=0, column=2)
    selection = conn.execute('SELECT * FROM TASKS')
    i = 1
    for name in selection:
        for j in range(len(name)):
            e = Entry(tab3, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, name[j])
        i = i + 1
    tab2canvas.configure(bg='#C3E8BD')
    createtaskbtn = Button(tab3, text="Создать задачу")
