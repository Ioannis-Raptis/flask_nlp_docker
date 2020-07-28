FROM python:3.8.2
WORKDIR /app
COPY ./requirements.txt /app

RUN pip install -r requirements.txt
COPY . /app

ENTRYPOINT ["python"]
CMD ["app.py"]