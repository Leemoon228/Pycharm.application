# -*- coding: cp1251 -*-

# import requests

import threading
import time
import tkinter as tk
from tkinter import ttk
from tkinter import *
from win10toast_click import ToastNotifier


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


# Здесь начинается окно
root = tk.Tk()
root.title('Reminder App v0.01')
root.geometry('+%d+%d' % (650, 340))

HealthReminding = threading.Thread(target=thread_function)
HealthReminding.start()  # Фоновое отображение уведомлений

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# Buttons
example_text = tk.StringVar()
example_btn = tk.Button(root, textvariable=example_text, command=lambda: open_body_healthcare_notif(),
                        font="Raleway",
                        bg="#20bebe",
                        fg="white",
                        height=2,
                        width=10)
example_text.set("Пример\nуведомления")
example_btn.grid(column=0, row=0)

entry_name = tk.Entry(root)
entry_def = tk.Entry(root)
button1 = tk.Button(text='Create your notification', command=create_notif, font="Raleway", bg="#20bebe", fg="white")

times = [0, 1, 3, 5, 10, 15, 30, 60]
box_text = IntVar()
combobox = ttk.Combobox(root, textvariable=box_text)
combobox['state'] = 'readonly'
combobox['values'] = times

canvas.create_text(480, 20, text="Через сколько секунд", fill="black")
canvas.create_window(480, 40, window=combobox)
canvas.create_text(480, 60, text="Введите название вашего уведомления", fill="black")
canvas.create_window(480, 80, window=entry_name)
canvas.create_text(480, 100, text="Введите описание вашего уведомления", fill="black")
canvas.create_window(480, 120, window=entry_def)
canvas.create_window(480, 170, window=button1)

root.mainloop()