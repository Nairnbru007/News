import requests
import asyncio
import threading, time
i=1;
def gg(i):
	print(str(i)+' START')
	r = requests.get('http://192.168.10.253/tass_news?url=https://tass.ru/ekonomika/18086135')
	print(str(i)+' OK')

if __name__ == "__main__":
	arr=[]
	for i in range(2):
		arr.append(threading.Thread(target=gg,args=(i,)))
	for i in arr:
		i.start()
	print(end - start)
	