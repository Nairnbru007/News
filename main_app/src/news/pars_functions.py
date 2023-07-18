from bs4 import BeautifulSoup
import time
import random
import re
from fake_useragent import UserAgent
import xmltodict, json

def emulator_runing(driver):
	for i in range(1,random.randint(2, 4)):
		driver.execute_script("window.scrollBy(0,"+str(random.randint(1, 250))+")")
		driver.execute_script("window.scrollBy(0,"+str(random.randint(-250, -1))+")")

def delete_tags(soup,class_="",id="",tag=""):
	try:
		if tag!="":
			if id!="":
				for i in soup.find_all(id=re.compile(id_)):
					i.decompose()
			elif class_!="":
				for i in soup.find_all(class_=re.compile(class_)):
					i.decompose()
			else:
				for i in soup.find_all(tag):
					i.decompose()
	except:
		pass



# tass.ru
def get_rss(url,driver,html=True):
	try:
		driver.get(url)
	except:
		return 'tass get rss ops'
	time.sleep(5)
	if html==True:
		result=driver.page_source#.encode("utf-8").decode("utf-8")
		return result
	else:
		result=json.dumps(xmltodict.parse(driver.page_source.encode("utf-8")))
		return result

def tass_get_news(url,driver,html=True):
	trying=0
	driver.get(url)
	try:
		driver.get(url)
	except:
		trying=1
	if trying==1:
		try:
			driver.get(url)
		except:
			return 'tass news ops'
	time.sleep(1)
	html = driver.page_source.encode("utf-8")
	soup = BeautifulSoup(html,"html.parser")

	####
	#soup.find('div', class_="roxotAdContainer").decompose()
	#delete_tags(soup,tag='div',class_="roxotAdContainer")
	#delete_tags(soup,id=r"inread-after\w+")
	####
	if html==True:
		result='<!DOCTYPE html><head><meta charset="UTF-8"></head><body>'
		for tag in soup.find_all('article'):
			result=result+str(tag)
		result=result+'</body></html>'
	else:
		result=json.dumps(xmltodict.parse('<e> <a>text</a> <a>text</a> </e>'))

		
	return result	

def rg_get_news(url,driver):
	#driver=init_driver()
	trying=0
	try:
		driver.get(url)
	except:
		trying=1
		#driver.close()
	if trying==1:
		try:
			driver.get(url)
		except:
			#driver.close()
			return 'rg get newsops'
	time.sleep(1)
	html = driver.page_source.encode("utf-8")
	#emulator_runing(driver)
	soup = BeautifulSoup(html,"html.parser")
	#driver.close()
	###
	delete_tags(soup,tag='rg-incut',class_="rg-incut")
	delete_tags(soup,tag='incut',class_="incut")
	delete_tags(soup,tag='div',class_=re.compile('.*Adfox_.*'))
	delete_tags(soup,tag='div',class_=re.compile('.*PageArticleContent_image_.*'))
	delete_tags(soup,tag='div',class_=re.compile('.*PageArticleContent_issue_.*'))
	delete_tags(soup,tag='div',class_=re.compile('.*PageArticle_partner_.*'))
	delete_tags(soup,tag='section',class_=re.compile('.*PageArticle_buttons.*'))
	delete_tags(soup,tag='div',class_=re.compile('.*ChannelButton_item_.*'))
	delete_tags(soup,tag='div',class_=re.compile('.*PageArticleContent_relationBottom_.*'))
	delete_tags(soup,tag='div',class_=re.compile('.*EditorialPageArticleContent_rubricsBottom_.*'))
	delete_tags(soup,tag='div',class_=re.compile('.*PageArticleContentSecondListPattern_wrapper_.*'))
	delete_tags(soup,tag='div',class_=re.compile('.*PageArticleContent_shareWrapper_.*'))
	delete_tags(soup,tag='div',class_=re.compile('.*PageArticleAside_.*'))
	#delete_tags(soup,tag='div',class_=re.compile('undefined.*'))
	delete_tags(soup,tag='div',class_=re.compile('.*Page_aside_.*'))
	delete_tags(soup,tag='div',class_=re.compile('.*LoadMoreBtn_.*'))
	delete_tags(soup,tag='div',class_=re.compile('.*PageArticleContent_authors_.*'))
	delete_tags(soup,tag='div',class_=re.compile('.*_imageWrapper__.*'))
	delete_tags(soup,tag='div',class_=re.compile('.*SujetMaterials_.*'))
	delete_tags(soup,tag='portal')
	delete_tags(soup,tag='button')
	delete_tags(soup,tag='path')
	###
	result='<!DOCTYPE html><head><meta charset="UTF-8"></head><body>'
	for tag in soup.find_all('div',class_=re.compile('.*Page_main_.*')):
		result=result+str(tag)
		#print('1')
		#print(tag)
	if result == '<!DOCTYPE html><head><meta charset="UTF-8"></head><body>':
		#print('2')
		for tag in soup.find_all('main'):
			result=result+str(tag)
	result=result+'</body></html>'
	return result
