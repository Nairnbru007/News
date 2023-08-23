FROM ubuntu

RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 \
    curl unzip wget software-properties-common\
    xvfb
    
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./main_app ./main_app
COPY requirements.txt main_app/
RUN pip3 install -r main_app/requirements.txt


WORKDIR /main_app/src