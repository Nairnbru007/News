FROM ubuntu

RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 \
    curl unzip wget software-properties-common\
    xvfb

RUN apt remove firefox -y
RUN add-apt-repository ppa:mozillateam/ppa -y
RUN apt install -t 'o=LP-PPA-mozillateam' firefox -y
#RUN echo 'Package: * ' | tee /etc/apt/preferences.d/mozilla-firefox
#RUN echo 'Pin: release o=LP-PPA-mozillateam' | tee /etc/apt/preferences.d/mozilla-firefox
#RUN echo 'Pin-Priority: 1001' | tee /etc/apt/preferences.d/mozilla-firefox
#RUN apt install -y firefox
RUN echo 'Unattended-Upgrade::Allowed-Origins:: "LP-PPA-mozillateam:${distro_codename}";' | tee /etc/apt/apt.conf.d/51unattended-upgrades-firefox


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./spider_app ./spider_app
COPY requirements.txt spider_app/
RUN pip3 install -r spider_app/requirements.txt


WORKDIR /spider_app/src


