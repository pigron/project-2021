FROM python:3.9
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /app
CMD uvicorn main:app --reload
EXPOSE 8000