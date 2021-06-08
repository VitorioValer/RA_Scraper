from collections import OrderedDict
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

PATH = './Driver/chromedriver'
URL = 'https://www.reclameaqui.com.br/'


def ra_scrapper(company_name):
	driver = webdriver.Chrome(PATH)
	driver.get(URL)

	sleep(2)

	cookies = driver.find_element_by_id('onetrust-accept-btn-handler')
	if cookies.is_displayed():
		WebDriverWait(driver, 10).until(
			EC.element_to_be_clickable((
				By.ID, 'onetrust-accept-btn-handler')
			)
		)

		cookies.click()

	search = driver.find_element_by_class_name('form-search')
	search.send_keys(company_name)

	sleep(.5)

	search.send_keys(Keys.RETURN)

	sleep(.5)

	element = driver.find_element_by_class_name('vueperslide--active')
	element.click()

	sleep(.5)

	data = OrderedDict()

	company_info = driver.find_element_by_class_name('info-wrapper').text
	company_info = company_info.split('\n')

	company_info = OrderedDict({
		'Nome': company_info[0].capitalize(),
		'Tempo': company_info[1],
		'Views': company_info[2]
	})

	about = driver.find_element_by_id('about').find_element_by_class_name(
		'sc-iQKALj').text

	about = about.split('\n')
	about.pop(-1)

	about = '\n'.join(about) if about else '-/-'

	company_info.update({'Brief:': about})

	data.update({
		'Sobre': company_info
	})

	reputation = driver.find_element_by_id('reputation')

	for i in range(1, 6):

		period = reputation.find_element_by_id(f'reputation-tab-{i}')

		period.click()
		sleep(1)

		info = driver.find_element_by_id('reputation').text.split('\n')
		scope = info[i]

		data.update({
			scope: OrderedDict({
				'Avaliação': info[6],
				'Período': info[9],
				'Score': f'{info[7]}{info[8]}'
			})
		})

		for i in range(10, 25, 2):
			data[scope].update({
				info[i]: info[i + 1]
			})

	driver.quit()

	return data

