FROM ubuntu:20.04
LABEL maintainer="Raymond Cao <raymond_cao@brown.edu>"
ENV TZ=America/New_York
RUN apt-get update -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-dev python3-pip ffmpeg nginx
RUN pip3 install uwsgi
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY ./nginx.conf /etc/nginx/sites-enabled/default
CMD service nginx start && uwsgi -s /tmp/uwsgi.sock --chmod-socket=666 --manage-script-name --mount /=app:app