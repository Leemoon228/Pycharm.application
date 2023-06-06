from win10toast_click import ToastNotifier
import threading
import time
import webbrowser
import sqlite3
from sqlite3 import Error
from tkinter import *
from tkinter.ttk import *
from threading import Timer
import tkcalendar
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count
from tkcalendar import Calendar
from datetime import date
import re
from datetime import datetime
notif_icon_path = "leaf3.ico"

def thread_function_One(delay_eyes=600):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        time.sleep(delay_eyes)
        open_eyes_healthcare_notif()


def thread_function_Two(delay_body=300):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        time.sleep(delay_body)
        open_body_healthcare_notif()


def validate(new_val):
    return re.match("^\d{0,2}\:[012345]?[0123456789]?$", new_val) is not None


def timer_stop(timer, func, duration_entry, sleep_entry):
    timer[0].cancel()
    timer[0] = RepeatTimer(1, func)
    duration_entry.config(state="normal")
    sleep_entry.config(state="normal")


def timer_start(duration_entry, sleep_entry, timer, current_text_lbl, current_time_lbl):
    if timer.is_alive():
        return
    dur_time = time_from_str(duration_entry.get())
    sleep_time = time_from_str(sleep_entry.get())
    duration_entry.config(state="disabled")
    sleep_entry.config(state="disabled")
    timer.daemon = True
    current_time_lbl.config(text=(str(dur_time // 60) + ":" +
                                  ("00" if ((str(dur_time % 60) ) == "0") else (str(dur_time % 60)))))
    timer.args = [current_text_lbl, current_time_lbl, dur_time, sleep_time]
    timer.start()


def label_change(text_lbl, time_lbl, base_dur_time=1800, base_sleep_time=300):
    cur_dur_time = time_from_str(time_lbl.cget("text"))
    cur_dur_time -= 1
    if cur_dur_time <= 0:
        if text_lbl.cget("text") == "Работа":
            notif_create("Пора отдохнуть",
                         "Помидорка работы прошла, пора взять перерыв и вернуться к работе после него")
            text_lbl.config(text="Отдых")
            time_lbl.config(text=(str(base_sleep_time // 60) + ":" +
                                  ("00" if ((str(base_sleep_time % 60) ) == "0") else (str(base_sleep_time % 60)))))
        else:
            notif_create("Пора работать",
                         "Помидорка отдыха прошла, возвращаемся к работе с новыми силами")
            text_lbl.config(text="Работа")
            time_lbl.config(text=(str(base_dur_time // 60) + ":" +
                                  ("00" if ((str(base_dur_time % 60) ) == "0") else (str(base_dur_time % 60)))))
    else:
        time_lbl.config(text=(str(cur_dur_time // 60) + ":" +
                              ("00" if ((str(cur_dur_time % 60) ) == "0") else (str(cur_dur_time % 60)))))


class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)


def notif_create(title, description, duration=10, icon=notif_icon_path, delay=0):
    toast = ToastNotifier()
    if delay != 0:
        def func(sleep_time, notif):
            time.sleep(sleep_time)
            notif.show_toast(title, description, duration=duration, threaded=True, icon_path=icon)

        thread = threading.Thread(target=func, args=[delay, toast], daemon=True)
        thread.start()
        return
    else:
        toast.show_toast(title, description, duration=duration, threaded=True, icon_path=icon)
    return


def time_from_str(time_string):
    first = time_string[0:time_string.find(':')]
    if first == '':
        first = "0"
    second = time_string[time_string.find(':') + 1:]
    if second == '':
        second = "0"
    time_in_seconds = int(first) * 60 + int(second)
    return time_in_seconds


def open_eyes_healthcare_notif():
    def open_eyes_healthcare():
        website = "https://www.wikihow.com/Exercise-Your-Eyes"
        try:
            webbrowser.open(website)
        except:
            print("Failed to open the download page.")

    toast = ToastNotifier()
    toast.show_toast("Пожалуйста дайте вашим глазам отдохнуть",
                     "Взгляните в даль, потом на палец, и закройте глаза на 20 секунд",
                     duration=8,
                     callback_on_click=open_eyes_healthcare,
                     threaded=True,
                     icon_path="leaf3.ico")


def open_body_healthcare():
    website = "https://ru.wikihow.com/выполнять-упражнения,-сидя-за-компьютером"
    try:
        webbrowser.open(website)
    except:
        print("Failed to open the download page.")


def open_body_healthcare_notif():
    toast2 = ToastNotifier()
    toast2.show_toast("Проведите разминку",
                      "Потратьте пару минут на разминку тела. Пример вы можете посмотреть нажав на уведомление",
                      duration=10,
                      callback_on_click=open_body_healthcare,
                      threaded=True,
                      icon_path="leaf3.ico")


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def openNewWindow(tab):
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(tab)

    # sets the title of the
    # Toplevel widget
    newWindow.title("Новая задача!! :3")
    newWindow.iconbitmap("leaf2.ico")
    newWindow.resizable(False, False)
    # sets the geometry of toplevel
    newWindow.geometry('+%d+%d' % (650, 340))
    windowCanvas = Canvas(newWindow, width=600, height=300)
    windowCanvas.grid(rowspan=5, columnspan=1)
    lName = Label(windowCanvas, text="Название задачи:", width=30).grid(row=0,column=0, columnspan=2)
    taskname = Text(windowCanvas, width=30, height=1)
    taskname.grid(row=1, column=0, columnspan=2)
    DateSet = tkcalendar.DateEntry(windowCanvas, selectmode='day')
    datevalid = StringVar()
    datevalid.set("Дедлайн:")
    lDate = Label(windowCanvas, textvariable=datevalid, width=30).grid(row=2, column=0, columnspan=2)
    DateSet.grid(row=3, column=0, columnspan=2)
    Button(newWindow, text="добавить", command=lambda: insertDB(taskname.get("1.0", END), DateSet.get_date(), datevalid, tab)).grid(row=5, column=0, columnspan=2)


def insertDB(taskname, DateSet, datevalid, tab):
    my_conn=sqlite3.connect('tasks.db')
    if DateSet<date.today():
        datevalid.set("Неверная дата, еще раз:")
        return print("wrong date, your date is"+DateSet.strftime("%Y-%m-%d"))
    my_data=(taskname, DateSet.strftime("%Y-%m-%d"), 0)
    my_query = "INSERT INTO tasks VALUES (?,?,?)"
    my_conn.execute(my_query,my_data)
    my_conn.commit()
    from program.tabs import filltab3
    filltab3(tab)
    return print("inserted")

def openEditWindow(tab, conn):
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(tab)
    selection = conn.execute('SELECT NAME, ROWID FROM TASKS WHERE NOROFY = 0')
    count = conn.execute('SELECT COUNT(ROWID) FROM TASKS WHERE NOROFY = 0').fetchone()[0]
    options = [0]*count
    optionsid = [0]*count
    j=0
    for name in selection:
        options[j]=name[0].split()
        optionsid[j]=name[1]
        j+=1
    #print(options)
    #print(optionsid)
    test = [0]*count
    for i in range(len(options)):
        test[i]=[optionsid[i],options[i]]
    #print(test)
    # sets the title of the
    # Toplevel widget
    newWindow.title("Отметить задачу!! :3")
    newWindow.iconbitmap("leaf2.ico")
    newWindow.resizable(False, False)
    # sets the geometry of toplevel
    newWindow.geometry('+%d+%d' % (650, 340))
    windowCanvas = Canvas(newWindow, width=600, height=300)
    windowCanvas.grid(columnspan=1)
    Label(windowCanvas, text="Название задачи:", width=30).grid(row=0, column=0, columnspan=2)
    clicked = StringVar()
    drop = OptionMenu(windowCanvas, clicked, test[0], *test)
    drop.grid(row=1, column=0)
    submitbtn = Button(windowCanvas, text="Отметить как выполненное", width=30, command=lambda: updateDB(conn, clicked.get(), tab))
    submitbtn.grid(row=2, column=0)

def updateDB(conn, rowid, tab):
    rowid = rowid[1:rowid.find(',')]
    my_query="UPDATE TASKS SET NOROFY = 1 WHERE ROWID ="+rowid
    conn.execute(my_query)
    conn.commit()
    from program.tabs import filltab3
    filltab3(tab)
    return print("updated")

def openDelWindow(tab, conn):
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(tab)
    selection = conn.execute('SELECT NAME, ROWID FROM TASKS')
    count = conn.execute('SELECT COUNT(ROWID) FROM TASKS').fetchone()[0]
    options = [0] * count
    optionsid = [0] * count
    j = 0
    for name in selection:
        options[j] = name[0].split()
        optionsid[j] = name[1]
        j += 1
    test = [0] * count
    for i in range(len(options)):
        test[i] = [optionsid[i], options[i]]

    # sets the title of the
    # Toplevel widget
    newWindow.title("Удалить задачу!! :3")
    newWindow.iconbitmap("leaf2.ico")
    newWindow.resizable(False, False)
    # sets the geometry of toplevel
    newWindow.geometry('+%d+%d' % (650, 340))
    windowCanvas = Canvas(newWindow, width=600, height=300)
    windowCanvas.grid(columnspan=1)
    Label(windowCanvas, text="Название задачи:", width=30).grid(row=0, column=0, columnspan=2)
    clicked = StringVar()
    drop = OptionMenu(windowCanvas, clicked, test[0], *test)
    drop.grid(row=1, column=0)
    submitbtn = Button(windowCanvas, text="Удалить задачу", width=30,
                       command=lambda: deleteDB(conn, clicked.get(), tab))
    submitbtn.grid(row=2, column=0)

def deleteDB(conn, rowid, tab):
    rowid = rowid[1:rowid.find(',')]
    my_query = "DELETE FROM TASKS WHERE ROWID =" + rowid
    conn.execute(my_query)
    conn.commit()
    from program.tabs import filltab3
    filltab3(tab)
    return print("updated")