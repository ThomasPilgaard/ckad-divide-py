FROM python:3.8
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY divideweb.py .
ENV FLASK_APP=divide-web.py
EXPOSE 5000
CMD [ "waitress-serve", "--call", "divideweb:create_app"]
