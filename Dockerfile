FROM python:3.9.0

RUN git clone https://github.com/KEEMSY/MUSCLE_MALL.git .

ADD requirements.txt .

CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]