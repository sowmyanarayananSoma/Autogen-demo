FROM ubuntu:latest
RUN apt update
RUN apt install python3 -y
RUN apt install -y python3-pip
WORKDIR /usr/app/src
COPY * ./
RUN pip install pyautogen
CMD ["python3","source/main.py"]