FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/KEEMSY/MUSCLE_MALL.git

WORKDIR /home/MUSCLE_MALL/

ADD requirements.txt .

CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]