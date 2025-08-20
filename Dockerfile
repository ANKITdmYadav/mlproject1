From python:3.8-slim-buster
WORKDIR /app
COPY . /app

# this will update all the packages and version which are we using
RUN apt update -y && apt install awscli -y

RUN pip install -r requirements.txt
CMD ["python3","app.py"]