from math import ceil
from os import path, mkdir

import xlsxwriter


def xlsx_writer(file_name, file_data):
    """
    Cria e escreve um arquivo xlsx contendo tabelas com as informaçẽos passadas
    :param file_name: nome do arquivo a ser gerado
    :param file_data: dicionário contando as informações a serem escritas no
    arquivo
    :return: None
    """

    # path do diretório onde arquivo será salvo
    dir_name = path.join(path.dirname(__file__), 'Resultados')
    # path do arquivo
    file_name = path.join(dir_name, f'{file_name}.xlsx')

    if not path.exists(dir_name):  # verifica a existência do diretório
        mkdir(dir_name)  # cria o diretório

    with xlsxwriter.Workbook(file_name) as workbook:  # cria o arquivo
        for sheet_name, sheet_data in file_data.items():
            worksheet = workbook.add_worksheet(name=sheet_name)  # cria página
            worksheet.set_column('A:B', 25)  # formata largura das colunas A e B

            for i, row in enumerate(sheet_data.items()):
                # define tamanho da altura da linha como proporcional ao
                # tamanho do texto contido nela
                size = ceil(len(''.join(row[1].split())) / 25)
                size = ceil(size / 1.5)
                size = 30 * size

                # define cor da célula
                color = '#b1b1b1' if i % 2 else '#747474'

                # define formatação da ceĺula
                cell_format = workbook.add_format({
                    'text_wrap': True,
                    'align': 'center',
                    'valign': 'vcenter',
                    'border': 6,
                    'bg_color': color
                })

                worksheet.set_row(i, size)  # formata altura da linha

                # escreve conteúdo da primeira coluna da linha
                worksheet.write(i, 0, row[0], cell_format)

                # dict contendo relação entre scores e cor da célula
                scores = {
                    'RA1000': '#4ad851',
                    'ÓTIMO': '#5fbe64',
                    'BOM': '#3c6b9c',
                    'REGULAR': '#d2d84a',
                    'RUIM': '#fb1b00',
                    'NÃO RECOMENDADA': '#8735bd'
                }

                # verifica se conteúdo da segunda coluna é um score
                if row[1] in scores:
                    #  reformata a célula de acordo com o score
                    cell_format = workbook.add_format({
                        'text_wrap': True,
                        'align': 'center',
                        'valign': 'vcenter',
                        'border': 6,
                        'bold': True,
                        'bg_color': scores[row[1]]
                    })

                # escreve conteúdo da segunda coluna da linha
                worksheet.write(i, 1, row[1], cell_format)

