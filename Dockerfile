FROM python:3.9
COPY . .
RUN pip install mysql-connector-python pandas Flask -U flask-cors flask-mysql
CMD ["python", "main.py"]
