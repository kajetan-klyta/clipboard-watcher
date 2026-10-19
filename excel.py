from openpyexcel import load_workbook
import textwrap

wb = load_workbook('nomenclature.xlsx')

ws = wb.active


def normalize_input(text):
    normalized_text = [char for char in text if char.isnumeric()]
    code = ''.join(normalized_text).replace(' ', '')
    if len(code) < 6 or len(code) > 10:
        return None
    elif len(code) in [7, 9]:
        return code[:-1]
    return code


def find_base_indent_desc(tariff):
    for row in range(2, 25000):
        if tariff[:4] in ws['A' + str(row)].value[:4] and not ws['F' + str(row)].value:
            return ws['G' + str(row)].value

    return None


def find_tariff(text):
    tariff = normalize_input(text)
    if tariff:
        for row in range(1, 27000):
            if tariff in ws['A' + str(row)].value:
                indent_level = ws['F' + str(row)].value
                if indent_level:
                    base_desc = find_base_indent_desc(tariff)
                    return f"""Tariff: {ws['A' + str(row)].value[:-3]}\n\nBase desc: {base_desc}\n\ndesc: {ws['G' + str(row)].value}
                    """
                return ws['A' + str(row)].value[:-3], ws['G' + str(row)].value

    return None


if __name__ == '__main__':
    for row in range(2, 20):
        print(ws['F' + str(row)].value)
