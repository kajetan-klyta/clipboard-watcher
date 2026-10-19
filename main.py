import pyperclip
import time
import subprocess
import platform
from excel import find_tariff

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
        result = find_tariff(current_text)
        if result:
            print(result)
        else:
            print('No result')
    else:
        continue
