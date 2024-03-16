FROM python:3.11.8

RUN mkdir /workspace
COPY . /workspace/
WORKDIR /workspace
RUN pip install -r requirements.txt


