FROM python:3.9

WORKDIR /home/plov06/kpi/qa-kp03-pavliushyn/sem_5_lab_3

COPY requirements.txt /home/plov06/kpi/qa-kp03-pavliushyn/sem_5_lab_3
RUN pip freeze > requirements.txt
RUN pip3 install flask
RUN pip3 install --upgrade pip -r requirements.txt

COPY . /home/plov06/kpi/qa-kp03-pavliushyn/sem_5_lab_3

EXPOSE 5000

CMD ["python", "app.py"]