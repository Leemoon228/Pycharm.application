# -*- coding: cp1251 -*-

# import requests
import webbrowser
import threading
import time
import tkinter as tk
from tkinter import ttk
from tkinter import *
from win10toast_click import ToastNotifier


# ������� ����� ����������� TODO
# https://stackoverflow.com/questions/65871197/python-winrt-windows-toast-notification-get-input-as-a-variable


# ������������ �������

def open_eyes_healthcare_notif():
    def open_eyes_healtcare():
        website = "https://www.wikihow.com/Exercise-Your-Eyes"
        try:
            webbrowser.open(website)
        except:
            print("Failed to open the download page.")

    toast = ToastNotifier()
    toast.show_toast("Please make your eyes heathy",
                     "Look into distance, then take a close loot at ur finger, close your eyes fo 20s",
                     duration=8,
                     callback_on_click=open_eyes_healtcare,
                     threaded=True,
                     icon_path="leaf2.ico")


def open_body_healthcare():
    website = "https://ru.wikihow.com/���������-����������,-����-��-�����������"
    try:
        webbrowser.open(website)
    except:
        print("Failed to open the download page.")


def open_body_healthcare_notif():
    toast2 = ToastNotifier()
    toast2.show_toast("��������� ��������",
                      "��������� ���� ����� �� �������� ����. ������ �� ������ ���������� ����� �� �����������",
                      duration=10,
                      callback_on_click=open_body_healthcare,
                      threaded=True,
                      icon_path="leaf2.ico")


def thread_function():
    while True:
        time.sleep(20)
        open_eyes_healthcare_notif()
        time.sleep(60)
        open_body_healthcare_notif()


def create_notif():
    name = entry_name.get()
    description = entry_def.get()
    user_toast = ToastNotifier()
    if name == "" or description == "":
        user_toast.show_toast("�� ����������� ������� ������ ��� �����������",
                              "������ ���� ������� ��������, �������� � ������������",
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


# ����� ���������� ����
root = tk.Tk()
root.title('Reminder App v0.01')
root.geometry('+%d+%d' % (650, 340))

HealthReminding = threading.Thread(target=thread_function)
HealthReminding.start()  # ������� ����������� �����������

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
example_text.set("������\n�����������")
example_btn.grid(column=0, row=0)

entry_name = tk.Entry(root)
entry_def = tk.Entry(root)
button1 = tk.Button(text='Create your notification', command=create_notif, font="Raleway", bg="#20bebe", fg="white")

times = [0, 1, 3, 5, 10, 15, 30, 60]
box_text = IntVar()
combobox = ttk.Combobox(root, textvariable=box_text)
combobox['state'] = 'readonly'
combobox['values'] = times

canvas.create_text(480, 20, text="����� ������� ������", fill="black")
canvas.create_window(480, 40, window=combobox)
canvas.create_text(480, 60, text="������� �������� ������ �����������", fill="black")
canvas.create_window(480, 80, window=entry_name)
canvas.create_text(480, 100, text="������� �������� ������ �����������", fill="black")
canvas.create_window(480, 120, window=entry_def)
canvas.create_window(480, 170, window=button1)

root.mainloop()