FROM python:3.7 as builder

WORKDIR /opt

COPY ./requirements.txt /opt/requirements.txt

RUN pip install -r requirements.txt

COPY . /opt

RUN  make -C ./content/en/ html &&  make -C ./content/zh/ html

FROM nginx

COPY --from=builder /opt/content/en/build/html  /usr/share/nginx/html/dongtai-doc/en/
COPY --from=builder /opt/content/zh/build/html  /usr/share/nginx/html/dongtai-doc/zh/

COPY ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

