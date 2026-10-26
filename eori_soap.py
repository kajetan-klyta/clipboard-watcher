import re, urllib.request
from colorama import Fore, Style, Back


def check_eori(eori: str):
    soap = ('<?xml version="1.0" encoding="UTF-8"?>'
            '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" '
            'xmlns:eor="http://eori.ws.eos.dds.s/"><soapenv:Body>'
            f'<eor:validateEORI><eor:eori>{eori}</eor:eori></eor:validateEORI>'
            '</soapenv:Body></soapenv:Envelope>')

    req = urllib.request.Request(
        "https://ec.europa.eu/taxation_customs/dds2/eos/validation/services/validation",
        data=soap.encode(),
        headers={"Content-Type": "text/xml; charset=utf-8",
                 "User-Agent": "clipboard-watcher/1.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        body = r.read().decode("utf-8", "replace")
    status = re.search(r"<status>(\d+)</status>", body)
    name = re.search(r"<name>([^<]*)</name>", body)
    return f"""EORI: {eori}\nSTATUS: {Back.GREEN + Fore.BLACK + 'valid' if status.group(1) == '0' else Back.RED + Fore.BLACK + 'not valid'}\n{Style.RESET_ALL}COMPANY: {name.group(1) if name else 'not shown'}
    """
