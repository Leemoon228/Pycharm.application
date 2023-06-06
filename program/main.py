# -*- coding: cp1251 -*-
# checkout 3
# test string
# import requests
from program.func import *
from program.tabs import filltab2, filltab3
import threading
import time
import tkinter as tk
from tkinter import ttk
from tkinter import *
from win10toast_click import ToastNotifier
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk



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


# Здесь начинается окно
root = tk.Tk()
root.title('Reminder App v0.02')
root.geometry('+%d+%d' % (650, 340))
root.iconbitmap("leaf2.ico")
root.resizable(False, False)
# Определение тем (стилей элементов)
style = ttk.Style()
style.configure(
    "Text.TLabel",
    foreground="black",
    font="Bahnschrift",
    background="#C3E8BD",
    fontsize=14
)
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = Frame(tabControl)
tabControl.add(tab1, text='Пример')
tabControl.add(tab2, text='Помидорки')
tabControl.add(tab3, text='Стикеры')
tabControl.pack(expand=2, fill="both")

HealthReminding = threading.Thread(target=thread_function, daemon=True)
HealthReminding.start()  # Фоновое отображение уведомлений

canvas = tk.Canvas(tab1, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)
canvas.configure(bg='#C3E8BD')

check = (tab1.register(validate), "%P")

#Window GIF
Window_lbl = ImageLabel(tab1)
Window_lbl.grid(row=0, column=2, columnspan=3, sticky="e", padx=5)
Window_lbl.configure(bg="#C3E8BD")
Window_lbl.load('window.gif')

# Buttons
example_btn = tk.Button(tab1, text="Проверка работы\nуведомлений", command=lambda: notif_create("Проверка уведомления",
                                                 "Если вы увидели это увдомление, то у вас всё работает прекрасно"),
                        font="Bahnschrift",
                        bg="#2e5339",
                        fg="#C3E8BD",
                        height=2,
                        width=15)



Time_delayed_lbl = ttk.Label(tab1, text="Время до\nуведомления", style="Text.TLabel", justify="center")
Time_delayed_entry = tk.Entry(tab1, validate="key", validatecommand=check, width=5,
                              font=("Bahnschrift", 15), background="#C3E8BD", justify="center",
                              selectborderwidth="0")
Time_delayed_entry.insert(0, "00:30")

button1 = tk.Button(text='Своё уведомление',
                    command=lambda: notif_create("Ваше уведомление",
                                                 "Вы откладывали уведомление чтобы о чём-то не забыть. Самое время чтобы вспомнить об этом",
                                                 delay=time_from_str(Time_delayed_entry.get())),
                    font="Bahnschrift", bg="#2e5339", fg="#C3E8BD")


canvas.create_window(90, 190, window=Time_delayed_lbl)
canvas.create_window(90, 230, window=Time_delayed_entry)
canvas.create_window(90, 270, window=button1)
canvas.create_window(300, 260, window=example_btn)


filltab2(tab2)
filltab3(tab3)
root.protocol('WM_DELETE_WINDOW', hide_window)

root.mainloop()
