FROM python:2.7

RUN pip install jupyter
RUN pip install pandas

WORKDIR /app
ADD start.sh /app/
CMD ["bash", "/app/start.sh"]