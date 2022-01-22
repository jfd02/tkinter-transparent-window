import tkinter as tk
import multiprocessing
from win32gui import SetWindowLong, GetWindowLong, SetLayeredWindowAttributes
from win32con import WS_EX_LAYERED, WS_EX_TRANSPARENT, GWL_EXSTYLE
from time import sleep
import datetime

MESSAGE_COUNT = 0


def set_clickthrough(hwnd):
    try:
        styles = GetWindowLong(hwnd, GWL_EXSTYLE)
        styles = WS_EX_LAYERED | WS_EX_TRANSPARENT
        SetWindowLong(hwnd, GWL_EXSTYLE, styles)
        SetLayeredWindowAttributes(hwnd, 0, 255, 0x00000001)
    except Exception as e:
        print(e)


def func1(message_queue):
    global MESSAGE_COUNT
    timestamp = datetime.datetime.now()
    f_timestamp = timestamp.strftime("%m/%d/%Y, %H:%M:%S")
    message_queue.put(("CONSOLE", f"{f_timestamp} Message {MESSAGE_COUNT}"))
    MESSAGE_COUNT += 1


def main(message_queue):
    while True:
        func1(message_queue)
        sleep(0.5)


def consume_text():
    if message_queue.empty() is False:
        message = message_queue.get()
        if 'CONSOLE' in message[0]:
            console.configure(state='normal')
            console.insert(tk.END, f'{message[1]}' + '\n')
            console.configure(state='disabled')
            console.yview(tk.END)

    root.after(ms=1, func=consume_text)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('1920x1080')
    root.overrideredirect(True)
    root.config(bg='#000000')
    root.attributes("-alpha", 1)
    root.wm_attributes("-topmost", 1)
    root.attributes('-transparentcolor', '#000000', '-topmost', 1)
    root.resizable(False, False)
    set_clickthrough(root.winfo_id())

    label = tk.Label(root, text="+", bg="black", fg="red", font=("Arial", 30), bd=0)
    label.place(x=1920 / 2, y=1080 / 2)

    console = tk.Text(root, state='disabled', width=50, height=10, bg="black", fg="red", bd=0)
    console.place(x=20, y=20)

    message_queue = multiprocessing.Queue()
    program_thread = multiprocessing.Process(target=main, args=(message_queue,))
    program_thread.start()

    consume_text()
    root.mainloop()
