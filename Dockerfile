FROM ubuntu:latest

RUN apt update -q && DEBIAN_FRONTEND=noninteractive apt install -qy ffmpeg git python3-pip awscli

ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /app
ADD whisper.py whisper.py

CMD python3 whisper.py