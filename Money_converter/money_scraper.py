from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def scrape_data(driver, amount, type, convert):

	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'amount')))
	set_amount_money = driver.find_element_by_id('amount').click()
	set_amount_money = driver.find_element_by_id('amount').send_keys(amount)

	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'midmarketFromCurrency')))
	set_type_money = driver.find_element_by_id('midmarketFromCurrency').click()
	set_type_money = driver.find_element_by_id('midmarketFromCurrency').send_keys(type, Keys.RETURN)

	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'midmarketToCurrency')))
	set_convert_money = driver.find_element_by_id('midmarketToCurrency').click()
	set_convert_money = driver.find_element_by_id('midmarketToCurrency').send_keys(convert, Keys.RETURN)

	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/section/div[2]/div/main/form/div[2]/button')))
	button_convert = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div[2]/section/div[2]/div/main/form/div[2]/button').click()

	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/section/div[2]/div/main/form/div[2]/div[1]/p[1]')))
	money_to_convert = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div[2]/section/div[2]/div/main/form/div[2]/div[1]/p[1]')

	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/section/div[2]/div/main/form/div[2]/div[1]/p[2]')))
	money_converted = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div[2]/section/div[2]/div/main/form/div[2]/div[1]/p[2]')

	return (money_converted.text, money_to_convert.text)