FROM python:3.9 
EXPOSE 8080 
USER root 
ENV INSTANA_SERVICE_NAME=payment 
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requiremts.txt
COPY *.py /app/
COPY payment.ini /app/
CMD ["UWSGI","--ini","payment.ini"]
