import pyperclip
import time
import subprocess
import platform
import re
from classes import TariffValidator, extract_tariff
from eori_soap import check_eori


def clear_terminal():
    if platform.system() == 'Windows':
        subprocess.run(['cls'], shell=True)
    else:
        subprocess.run(['clear'], shell=False)


def check_eori_format(text):
    e = re.sub(r"[\s\-\.]", "", text or "").upper()

    prefixes = ['GB', 'XI', 'DE', 'FR', 'NL', 'BE', 'IE', 'IT', 'ES', 'PL', 'SE', 'AT']

    if re.match(r"^[A-Z]{2}[A-Z0-9]{1,15}$", e):
        if e[:2] in prefixes:
            return e

    return None


previous_text = pyperclip.paste()
tariff_validator = TariffValidator()

while True:
    time.sleep(0.5)
    current_text = pyperclip.paste()

    # if change in clipboard
    if current_text != previous_text:
        clear_terminal()
        # overwrite previous input
        previous_text = current_text

        eori = check_eori_format(current_text)
        if eori:
            result = check_eori(eori)
            print(result)
            continue

        # search tariff in excel sheet
        tariff = extract_tariff(current_text)
        if tariff:
            result = tariff_validator.find_tariff(tariff)
            if result:
                print(result)
            else:
                print(f'Invalid tariff: {tariff}')

        else:
            print(f'Query: {current_text}')
            print('No result')
    else:
        continue
