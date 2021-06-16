from money_parser import parse_data
from money_scraper import scrape_data
from selenium import webdriver
from plyer import notification
from time import sleep

if __name__ == '__main__':
	args = parse_data()
	url = 'https://www.xe.com/currencyconverter/'
	driver = webdriver.Chrome(r'C:\chromedriver.exe')
	driver.get(url)
	#driver.minimize_window()

	if args['type'].find('s', len(args['type'])-1) > len(args['type'])-2:
		args['type'] = args['type'][:-1]
	if args['convert'].find('s', len(args['convert'])-1) > len(args['convert'])-2:
		args['convert'] = args['convert'][:-1]

	converted, to_convert = scrape_data(driver, args['money'], args['type'], args['convert'])

	notification.notify(
		title = 'Money converter',
		message = '{} {}'.format(to_convert, converted),
		app_icon = 'favicon.ico'

		)

	sleep(5)
	driver.close()