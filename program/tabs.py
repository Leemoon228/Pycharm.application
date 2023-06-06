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

from datetime import datetime


def filltab2(tab2):
    tab2canvas = tk.Canvas(tab2, width=600, height=300)
    tab2canvas.configure(bg='#C3E8BD')
    tab2canvas.grid(columnspan=3, rowspan=4)
    check = (tab2.register(validate), "%P")

    heading_lbl = ttk.Label(tab2, text="Помидорковый таймер", style="Text.TLabel")
    heading_lbl.grid(column=1, row=0, sticky="n", pady="2")

    TimeDuration_lbl = ttk.Label(tab2, text="Длительность \nработы", style="Text.TLabel")
    TimeDuration_lbl.grid(column=0, row=0, sticky="nw", pady="65", padx=2)
    TimeDuration_entry = tk.Entry(tab2, validate="key", validatecommand=check, width=5,
                                  font=("Bahnschrift", 15), background="#C3E8BD", justify="center",
                                  selectborderwidth="0")
    TimeDuration_entry.insert(0, "30:00")
    TimeDuration_entry.grid(column=0, row=0, rowspan=2, sticky="nw", pady="105", padx="16")

    TimeBreak_lbl = ttk.Label(tab2, text="Длительность \nперерыва", style="Text.TLabel")
    TimeBreak_lbl.grid(column=0, row=0, rowspan=2, sticky="sw", pady="50", padx=2)
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

    Tomato_Timer = [RepeatTimer(1, label_change)]

    # Buttons
    start_btn = tk.Button(tab2, text="Старт",
                          font="Bahnschrift",
                          bg="#2e5339",
                          fg="#C3E8BD",
                          height=1,
                          width=7,
                          command=lambda: timer_start(TimeDuration_entry, TimeSleeping_entry, Tomato_Timer[0],
                                                      CurrentTimer_lbl, CurrentTimerTime_lbl))
    start_btn.grid(column=1, row=0, sticky="n", pady="30")
    pause_btn = tk.Button(tab2, text="Стоп",
                          font="Bahnschrift",
                          bg="#2e5339",
                          fg="#C3E8BD",
                          height=1,
                          width=7,
                          command=lambda: timer_stop(Tomato_Timer, label_change, TimeDuration_entry,
                                                     TimeSleeping_entry))
    pause_btn.grid(column=2, row=0, sticky="n", pady="30")
    # stop_btn = tk.Button(tab2, text="Стоп", font="Bahnschrift", bg="#2e5339", fg="#C3E8BD", height=1, width=7)
    # stop_btn.grid(column=0, row=3, sticky="sw", pady="10", padx="30")
    return


def filltab3(tab3):
    for widget in tab3.winfo_children():
        widget.destroy()
    conn = sqlite3.connect('tasks.db')
    rowspan = conn.execute('SELECT COUNT(ROWID) FROM TASKS').fetchone()[0]
    tab3.configure(relief=FLAT, bg="#C3E8BD")
    #create canvas in tab3 frame
    tab2canvas = tk.Canvas(tab3, bg="#C3E8BD", relief=FLAT, highlightthickness=0, height=250)
    tab2canvas.grid(row=1, columnspan=3, sticky='news')
    #create scrollbar in tab3 frame
    scroll = Scrollbar(tab3, orient="vertical", command=tab2canvas.yview, relief=FLAT)
    scroll.grid(row=1, column=3, sticky=NS)
    tab2canvas.configure(yscrollcommand=scroll.set)
    l1 =Label(tab3, text="Название", width=27, bg="#C3E8BD")
    l1.grid(row=0, column=0)
    l2 =Label(tab3, text="Истекает до", width=27, bg="#C3E8BD")
    l2.grid(row=0, column=1)
    l3 =Label(tab3, text="Уведомлять", width=27, bg="#C3E8BD")
    l3.grid(row=0, column=2)
    selection = conn.execute('SELECT * FROM TASKS')
    i=1
    table = Frame(tab2canvas)
    for name in selection:
        for j in range(len(name)):
             e = Entry(table, width=35, fg='blue', relief=tk.RIDGE)
             e.grid(row=i, column=j)
             if name[j]==0:
                e.insert(END, "не уведомлять")
             elif name[j]==1:
                e.insert(END, "уведомлять")
             else:
                e.insert(END, name[j])
        i=i+1
    table.update_idletasks()
    tab2canvas.create_window((0,0), window=table, anchor=NW)
    tab2canvas.configure(scrollregion=tab2canvas.bbox(ALL))
    createtaskbtn = Button(tab3, text="Создать задачу", command=lambda: openNewWindow(tab3))
    createtaskbtn.grid(row=rowspan+1, columnspan=3)


