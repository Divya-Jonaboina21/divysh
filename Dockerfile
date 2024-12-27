FROM python:3.61 
COPY . /app
WORKDIR /app
EXPOSE 5000 
RUN pip install -r requirements.txt 
ENTRUPOINT ["python","app.py"]
