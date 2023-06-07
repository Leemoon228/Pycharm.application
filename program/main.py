# -*- coding: cp1251 -*-
import tkcalendar
import re
import time
import webbrowser
from func import *
from tabs import filltab2, filltab3
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import *
import pystray
from sqlite3 import Error
from tkinter import *
from tkinter.ttk import *
from threading import Timer
from itertools import count
from datetime import date
from win10toast_click import ToastNotifier
from func import *
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image
import sqlite3


def change_threads(threads, eyes_time, body_time):
    threads[0].do_run = False
    threads[1].do_run = False
    threads[0] = threading.Thread(target=lambda: thread_function_One(time_from_str(eyes_time)), daemon=True)
    threads[1] = threading.Thread(target=lambda: thread_function_Two(time_from_str(body_time)), daemon=True)
    threads[0].start()
    threads[1].start()
    notif_create("����� ����������� �������� �������", "")



def show_window(icon, item):
    icon.stop()
    root.after(0, root.deiconify())
    root.focus_force()


def hide_window():
    root.withdraw()
    image = Image.open("leaf2.ico")
    menu = (pystray.MenuItem('Show', show_window, default=True), pystray.MenuItem('Quit', quit_window))
    icon = pystray.Icon("name", image, "Reminder App", menu)
    icon.run()


def quit_window(icon, item):
    icon.stop()
    root.destroy()


# ����� ���������� ����
root = tk.Tk()
root.title('Reminder App v0.88')
root.geometry('+%d+%d' % (650, 340))
root.iconbitmap("leaf2.ico")
root.resizable(False, False)
# ����������� ��� (������ ���������)
style = ttk.Style()
style.configure(
    "Text.TLabel",
    foreground="black",
    font="Bahnschrift",
    background="#C3E8BD",
    fontsize=14
)
style = ttk.Style()
style.configure(
    "TMenubutton",
    font="Bahnschrift",
    background="#C3E8BD",
    fontsize=10
)
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = Frame(tabControl)
tabControl.add(tab1, text='�������')
tabControl.add(tab2, text='���������')
tabControl.add(tab3, text='������')
tabControl.pack(expand=2, fill="both")

check = (tab1.register(validate), "%P")  # ��������� ������ �������

# ������� ����������� �����������
HealthRemindingOne = threading.Thread(target=thread_function_One, daemon=True)
HealthRemindingOne.start()
HealthRemindingTwo = threading.Thread(target=thread_function_Two, daemon=True)
HealthRemindingTwo.start()

canvas = tk.Canvas(tab1, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)
canvas.configure(bg='#C3E8BD')

Time_delayed_eyes_lbl = ttk.Label(tab1, text="����� �����������\n� �������� ����", style="Text.TLabel", justify="left")
Time_delayed_eyes_entry = tk.Entry(tab1, validate="key", validatecommand=check, width=5,
                                   font=("Bahnschrift", 15), background="#C3E8BD", justify="center",
                                   selectborderwidth="0")
Time_delayed_eyes_entry.insert(0, "15:00")

Time_delayed_body_lbl = ttk.Label(tab1, text="����� �����������\n� �������� ����", style="Text.TLabel", justify="left")
Time_delayed_body_entry = tk.Entry(tab1, validate="key", validatecommand=check, width=5,
                                   font=("Bahnschrift", 15), background="#C3E8BD", justify="center",
                                   selectborderwidth="0")
Time_delayed_body_entry.insert(0, "30:00")

# Window GIF
Window_lbl = ImageLabel(tab1, bg="#C3E8BD")
Window_lbl.grid(row=0, column=2, columnspan=3, sticky="e", padx=5)
Window_lbl.load('window.gif')

# Buttons
example_btn = tk.Button(tab1, text="�������� ������\n�����������", command=lambda: notif_create("�������� �����������",
                                                                                                "���� �� ������� ��� �����������, �� � ��� �� �������� ���������"),
                        font="Bahnschrift",
                        bg="#2e5339",
                        fg="#C3E8BD",
                        height=2,
                        width=15)

Time_delayed_lbl = ttk.Label(tab1, text="����� ��\n�����������", style="Text.TLabel", justify="center")
Time_delayed_entry = tk.Entry(tab1, validate="key", validatecommand=check, width=5,
                              font=("Bahnschrift", 15), background="#C3E8BD", justify="center",
                              selectborderwidth="0")
Time_delayed_entry.insert(0, "00:30")

button1 = tk.Button(text='��� �����������',
                    command=lambda: notif_create("���� �����������",
                                                 "�� ����������� ����������� ����� � ���-�� �� ������. ����� ����� ����� ��������� �� ����",
                                                 delay=time_from_str(Time_delayed_entry.get())),
                    font="Bahnschrift", bg="#2e5339", fg="#C3E8BD")

button_threads = tk.Button(tab1, text="������� �����\n�����������",
                           font="Bahnschrift",
                           bg="#2e5339",
                           fg="#C3E8BD",
                           height=2,
                           width=15,
                           command=lambda: change_threads([HealthRemindingOne, HealthRemindingTwo], Time_delayed_eyes_entry.get(), Time_delayed_body_entry.get()))

canvas.create_window(90, 190, window=Time_delayed_lbl)
canvas.create_window(90, 230, window=Time_delayed_entry)
canvas.create_window(90, 270, window=button1)
canvas.create_window(300, 260, window=example_btn)

canvas.create_window(150, 28, window=Time_delayed_eyes_lbl)
canvas.create_window(35, 30, window=Time_delayed_eyes_entry)

canvas.create_window(150, 78, window=Time_delayed_body_lbl)
canvas.create_window(35, 80, window=Time_delayed_body_entry)

canvas.create_window(90, 132, window=button_threads)

filltab2(tab2)
filltab3(tab3)
root.protocol('WM_DELETE_WINDOW', hide_window)

root.mainloop()
