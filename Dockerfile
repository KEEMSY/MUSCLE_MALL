FROM python:3.9.0

WORKDIR /home/mm/

RUN git clone https://github.com/KEEMSY/MUSCLE_MALL.git

ADD requirements.txt .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:5000"]