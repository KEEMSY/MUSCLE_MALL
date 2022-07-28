FROM python:3.9.0

WORKDIR /home/mm/

RUN git clone https://github.com/KEEMSY/MUSCLE_MALL.git

ADD requirements.txt .

CMD ["MM.wsgi", "--bind", "0.0.0.0:8000"]