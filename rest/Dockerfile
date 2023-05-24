FROM ubuntu:22.04

#Om zeker te zijn dat niets interactief draait
ARG DEBIAN_FRONTEND=noninteractive

#Installeer update met een && en dan install. 
#Dan worden de laatste packages gebruikt bij install
RUN apt-get update -y && apt-get upgrade -y && apt-get install -y \
  net-tools \
  iputils-ping \
  curl \
  lsb-release \
  lsb-core \
  nano \
  python3 \
  python3-pip

#installeer flask voor de rest service functionaliteit
RUN pip3 install flask
RUN pip3 install flask-restful

#maak de directory waar de restservice.py komt
#hier moet het volume op gemapped worden 
RUN mkdir /restservice
COPY restservice.py /restservice/
#start de restservice. standaard luister deze op poort 5000
CMD python3 /restservice/restservice.py
