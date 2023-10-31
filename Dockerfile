FROM python:3.11.5

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]

