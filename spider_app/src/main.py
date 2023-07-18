from fastapi import FastAPI,Depends
from fastapi import Response

import driver.driver as driver_
from news.router import main_pages_news_router,current_news_router
#from auth.router import user_main_router
#http://localhost:8000/docs


app_spider = FastAPI(
	title="Internet news",
	description="Welcome to News's API documentation!",
	)

driver=driver_.DRIVER

app_spider.include_router(
    main_pages_news_router, tags=["Main Pages of news"]
)

app_spider.include_router(
    current_news_router, tags=["Get the current news by URL"]
)

#app_spider.include_router(
#    user_main_router, tags=["Users"]
#)

