FROM python:3.7-alpine3.10
ARG dir=/opt/app

ADD demo ${dir}/demo
ADD requirements.txt ${dir}/requirements.txt
ADD run.sh ${dir}/run.sh

WORKDIR ${dir}


RUN apk add gcc libevent-dev
RUN pip install -r requirements.txt
gunicorn -b 127.0.0.1:8081 --worker-class=gevent --workers=4 demo:init_app