FROM ubuntu:18.04
WORKDIR /app
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev python3

# COPY form.html /app/form.html

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app
# Command to run on container start    
EXPOSE 8000
CMD [ "python" , "./main.py" ]