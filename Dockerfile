FROM python:3.8-slim
RUN mkdir "app"
COPY lib/ ./app/lib/
COPY src/ ./app/src/
COPY ./requirements.txt ./app/requirements.txt

RUN pip install app/lib \
    && pip install -r ./app/requirements.txt

RUN cd app/src \
    && mkdir "allure"