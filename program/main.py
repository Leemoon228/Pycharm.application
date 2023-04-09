# -*- coding: cp1251 -*-
# checkout 2
# import requests
from program.func import *
from program.tab2 import filltab2
import threading
import time
import tkinter as tk
from tkinter import ttk
from tkinter import *
from win10toast_click import ToastNotifier
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk


# сделать такие уведомления TODO
# https://stackoverflow.com/questions/65871197/python-winrt-windows-toast-notification-get-input-as-a-variable


# Используемые функции (привязанные к кнопкам)

def create_notif():
    name = entry_name.get()
    description = entry_def.get()
    user_toast = ToastNotifier()
    if name == "" or description == "":
        user_toast.show_toast("Вы неправильно указали данные для уведомления",
                              "Должны быть указаны название, описание и длительность",
                              duration=10,
                              threaded=True,
                              icon_path="leaf2.ico")
        return

    def user_notif():
        seconds = box_text.get()
        time.sleep(seconds)
        user_toast.show_toast(name, description,
                              duration=10,
                              threaded=True,
                              icon_path="leaf2.ico")

    notif = threading.Thread(target=user_notif)
    notif.start()


def show_window(icon, item):
    icon.stop()
    root.after(0, root.deiconify())


def hide_window():
    root.withdraw()
    image = Image.open("leaf2.ico")
    menu = (item('Show', show_window), item('Quit', quit_window))
    icon = pystray.Icon("name", image, "Reminder App", menu)
    icon.run()


def quit_window(icon, item):
    icon.stop()
    root.destroy()


# Здесь начинается окно
root = tk.Tk()
root.title('Reminder App v0.02')
root.geometry('+%d+%d' % (650, 340))
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tabControl.add(tab2, text='Tab 2')
tabControl.pack(expand=1, fill="both")
filltab2(tab2)
HealthReminding = threading.Thread(target=thread_function)
root.iconbitmap("leaf2.ico")

HealthReminding = threading.Thread(target=thread_function, daemon=True)
HealthReminding.start()  # Фоновое отображение уведомлений

canvas = tk.Canvas(tab1, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# Buttons
example_text = tk.StringVar()
example_btn = tk.Button(tab1, textvariable=example_text, command=lambda: open_body_healthcare_notif(),
                        font="Raleway",
                        bg="#20bebe",
                        fg="white",
                        height=2,
                        width=10)
example_text.set("Пример\nуведомления")
example_btn.grid(column=0, row=0)

entry_name = tk.Entry(tab1)
entry_def = tk.Entry(tab1)
button1 = tk.Button(text='Create your notification', command=create_notif, font="Raleway", bg="#20bebe", fg="white")

times = [0, 1, 3, 5, 10, 15, 30, 60]
box_text = IntVar()
combobox = ttk.Combobox(tab1, textvariable=box_text)
combobox['state'] = 'readonly'
combobox['values'] = times

canvas.create_text(480, 20, text="Через сколько секунд", fill="black")
canvas.create_window(480, 40, window=combobox)
canvas.create_text(480, 60, text="Введите название вашего уведомления", fill="black")
canvas.create_window(480, 80, window=entry_name)
canvas.create_text(480, 100, text="Введите описание вашего уведомления", fill="black")
canvas.create_window(480, 120, window=entry_def)
canvas.create_window(480, 170, window=button1)

root.protocol('WM_DELETE_WINDOW', hide_window)

root.mainloop()
