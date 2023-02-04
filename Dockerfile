FROM ubuntu:18.04
WORKDIR /app
RUN apt-get update -y
RUN apt-get install -y python3.8 python3-pip

COPY requirements.txt /app/requirements.txt
RUN python3.8 --version
RUN python3.8 -m pip install -r requirements.txt
COPY . /app

EXPOSE 8000
CMD [ "python3.8" , "./main.py" ]