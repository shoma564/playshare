FROM ubuntu:18.04


RUN apt -y update
RUN apt -y install python3 python3-pip curl wget
RUN apt autoremove
RUN pip3 install --upgrade pip setuptools


RUN mkdir -p /usr/src/app/
ADD ./requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

EXPOSE 5000

WORKDIR /usr/src/app/
CMD ["python3", "/usr/src/app/app.py"]
