from win10toast_click import ToastNotifier
import threading
import time
import webbrowser
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
                      icon_path="leaf2.ico")


def thread_function():
    while True:
        time.sleep(20)
        open_eyes_healthcare_notif()
        time.sleep(60)
        open_body_healthcare_notif()



