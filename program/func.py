from win10toast_click import ToastNotifier
import threading
import time
import webbrowser
import sqlite3
from sqlite3 import Error

notif_icon_path = "leaf3.ico"


def notif_create(title, description, duration=10, icon=notif_icon_path, delay=0):
    toast = ToastNotifier()
    if delay != 0:
        def func(sleep_time, notif):
            time.sleep(sleep_time)
            notif.show_toast(title, description, duration=duration, threaded=True, icon_path=icon)
        thread = threading.Thread(target=func, args=[delay, toast],  daemon=True)
        thread.start()
        return
    else:
        toast.show_toast(title, description, duration=duration, threaded=True, icon_path=icon)
    return


def thread_function(delay_eyes=300, delay_body=300):
    while True:
        time.sleep(delay_eyes)
        open_eyes_healthcare_notif()
        time.sleep(delay_body)
        open_body_healthcare_notif()


def open_eyes_healthcare_notif():
    def open_eyes_healthcare():
        website = "https://www.wikihow.com/Exercise-Your-Eyes"
        try:
            webbrowser.open(website)
        except:
            print("Failed to open the download page.")

    toast = ToastNotifier()
    toast.show_toast("Please make your eyes healthy",
                     "Look into distance, then take a close loot at ur finger, close your eyes fo 20s",
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