import win10toast
import time

toaster = win10toast.ToastNotifier()

while True:
    time.sleep(60) #Delay for 1 minute (60 sec)
    toaster.show_toast("python","success ! This is working!", duration=20)