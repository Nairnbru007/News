from fastapi import APIRouter, Depends,Response
from news.pars_functions import get_rss,rg_get_news,tass_get_news
import sys
sys.path.append("..")
from driver.driver import DRIVER

main_pages_news_router=APIRouter()
current_news_router=APIRouter()

driver = DRIVER

@main_pages_news_router.get('/api/tass')#+
def tass_rss():
   res=get_rss(url="http://tass.ru/rss/v2.xml",driver=driver,html=False)
   return Response(content=res, media_type='application/json')

@main_pages_news_router.get('/api/iz')#+
def rg_rss():
   res=get_rss(url="https://iz.ru/xml/rss/all.xml",driver=driver,html=False)
   return Response(content=res, media_type='application/json')

@main_pages_news_router.get('/api/rg')#+
def rg_rss():
   res=get_rss(url="https://rg.ru/xml/index.xml",driver=driver,html=False)
   return Response(content=res, media_type='application/json')



@current_news_router.get('/api/rg_news')
def rg_news():
   url = request.args.get('url')
   return rg_get_news(url=url,driver=driver)

@current_news_router.get('/api/tass_news')
def tass_news(url: str = None):
   return tass_get_news(url=url,driver=driver)


