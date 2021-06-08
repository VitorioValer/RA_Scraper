#!/usr/bin/env python

from ra_scraper import ra_scrapper
from xlsx_writer import xlsx_writer


def main():
	company = input('Informe o nome da empresa desejada -> ').strip()

	print('Procurando informações online. Por Favor aguarde...')

	xlsx_writer(
		file_name='_'.join(company.lower().split()),
		file_data=ra_scrapper(company)
	)

	print(
		'Informações coletadas com sucesso, novo arquivo foi gerado na pasta '
		'"Resultados".'
	)


if __name__ == '__main__':
	main()
