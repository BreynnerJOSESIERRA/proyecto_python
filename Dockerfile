FROM python:3.9-slim

WORKDIR /User/app/

COPY /app /User/app/

RUN pip install -r requeriments.txt 

CMD ["python", "server.py"]


