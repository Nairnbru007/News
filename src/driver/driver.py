import os
import sys
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


def init_driver(headless=True):
	if os.name == 'nt':
		# win 7
		PATH_TO_DRIVER = r'C:/test/slava/geck/geckodriver.exe'#os.path.join(os.getcwd(),'/geck/geckodriver.exe')
	elif os.name == 'posix':
		# linux
		PATH_TO_DRIVER = r'/home/user/rssgen/slava/geck/geckodriver'
	else:
		sys.exit(1)

	options = webdriver.FirefoxOptions()
	if headless==True:
		options.add_argument("--headless")
		options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
		service = Service(executable_path=PATH_TO_DRIVER)
		driver = webdriver.Firefox(service=service,options=options)
	else:
		options.add_argument("--headless")
		useragent = UserAgent()
		profile = webdriver.FirefoxProfile()
		profile.set_preference("general.useragent.override", useragent.random)
		profile.set_preference("javascript.enabled", False)

		profile.set_preference('browser.download.folderList', 2) # custom location
		profile.set_preference('browser.download.manager.showWhenStarting', False)
		profile.set_preference('browser.download.dir', '.')
		profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')

		options.add_argument("--width=2560")
		options.add_argument("--height=1440")
		driver = webdriver.Firefox(firefox_profile=profile,executable_path=PATH_TO_DRIVER,options=options)
		#driver = webdriver.Firefox(options=options)
	driver.set_page_load_timeout(40)
	driver.implicitly_wait(15)
	return driver
global driver
try:
	driver=init_driver()
	print('--SELENIUM driver RUN--')
except:
	print('--ERROR SELENIUM driver COULD NOT RUN--')