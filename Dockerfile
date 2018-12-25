FROM python:3.6-alpine

ADD requirements.txt /
RUN pip3 install -r requirements.txt

COPY . /parseInst
WORKDIR /parseInst

# ENV PATH="/parseInst/html_parser/geckodriver:${PATH}"

EXPOSE 5000
ENTRYPOINT ["python3.6", "/parseInst/app.py"]