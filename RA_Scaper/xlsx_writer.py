from math import ceil
from os import path, mkdir

import xlsxwriter


def xlsx_writer(file_name, file_data):
    dir_name = 'Resultados'
    file_name = path.join(dir_name, f'{file_name}.xlsx')

    if not path.exists(dir_name):
        mkdir(dir_name)

    with xlsxwriter.Workbook(file_name) as workbook:
        for sheet_name, sheet_data in file_data.items():
            worksheet = workbook.add_worksheet(name=sheet_name)
            worksheet.set_column('A:B', 25)

            for i, row in enumerate(sheet_data.items()):
                size = ceil(len(''.join(row[1].split())) / 25)
                size = ceil(size / 1.5)
                size = 30 * size

                color = '#b1b1b1' if i % 2 else '#747474'

                cell_format = workbook.add_format({
                    'text_wrap': True,
                    'align': 'center',
                    'valign': 'vcenter',
                    'border': 6,
                    'bg_color': color
                })

                worksheet.set_row(i, size)

                worksheet.write(i, 0, row[0], cell_format)

                scores = {
                    'RA1000': '#4ad851',
                    'ÓTIMO': '#5fbe64',
                    'BOM': '#3c6b9c',
                    'REGULAR': '#d2d84a',
                    'RUIM': '#fb1b00',
                    'NÃO RECOMENDADA': '#8735bd'
                }

                if row[1] in scores:

                    cell_format = workbook.add_format({
                        'text_wrap': True,
                        'align': 'center',
                        'valign': 'vcenter',
                        'border': 6,
                        'bold': True,
                        'bg_color': scores[row[1]]
                    })

                worksheet.write(i, 1, row[1], cell_format)

