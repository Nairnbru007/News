from fastapi import FastAPI,Depends
from fastapi import Response
from auth.router import user_main_router
#from news.router import main_pages_news_router,current_news_router

app_news = FastAPI(
	title="Internet news",
	description="Welcome to News's API documentation!",
	)

app_news.include_router(
   user_main_router, tags=["Users"]
)

# app_news.include_router(
#     main_pages_news_router, tags=["Main Pages of news"]
# )


