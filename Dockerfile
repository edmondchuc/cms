FROM python:3-alpine

WORKDIR /home

RUN apk add git

RUN git clone https://github.com/edmondchuc/cms.git

RUN pip3 install --upgrade pip

WORKDIR /home/cms

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]