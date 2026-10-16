import pyperclip
import time
import subprocess
import platform

def clear_terminal():
    if platform.system() == 'Windows':
        subprocess.run(['cls'], shell=True)
    else:
        subprocess.run(['clear'], shell=False)

previous_text = pyperclip.paste()

while True:
    time.sleep(0.5)
    current_text = pyperclip.paste()
    if current_text != previous_text:
        clear_terminal()
        previous_text = current_text
        print(current_text, end='', flush=True)
    else:
        continue