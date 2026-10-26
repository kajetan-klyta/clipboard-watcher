from openpyexcel import load_workbook


def extract_tariff(text: str):
    extracted_tariff = [char for char in text if char.isnumeric()]
    tariff = ''.join(extracted_tariff)

    if tariff == '' or len(tariff) < 6 or len(tariff) > 10:
        return None

    return tariff


class TariffValidator:

    def __init__(self):
        self.wb = load_workbook('nomenclature.xlsx')
        self.ws = self.wb.active

    def tariff_in_row(self, row):
        return self.ws['A' + str(row)].value

    def find_base_indent_desc(self, tariff):
        for row in range(2, 28000):
            if self.tariff_in_row(row):
                if tariff[:4] in self.ws['A' + str(row)].value[:4] and not self.ws['F' + str(row)].value:
                    return self.ws['G' + str(row)].value

        return None

    def find_tariff(self, tariff):
        for row in range(1, 28000):
            if self.tariff_in_row(row):
                if tariff in self.ws['A' + str(row)].value:
                    indent_level = self.ws['F' + str(row)].value
                    if indent_level:
                        base_desc = self.find_base_indent_desc(tariff)
                        return f"""TARIC: {self.ws['A' + str(row)].value[:-3]}\n\n- {base_desc}\n\n{indent_level}{self.ws['G' + str(row)].value}
                        """
                    return f"""TARIC: {self.ws['A' + str(row)].value[:-3]}\n\n{self.ws['G' + str(row)].value}
                        """

        return None
