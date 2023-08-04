FROM python:3-alpine3.10
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENV temp_user = testing_user
ENV passkey = z1PQauFiXvOl5qpw
CMD python ./app.py