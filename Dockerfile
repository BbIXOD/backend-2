FROM python:3.11.3-alpine

WORKDIR /app

ENV TZ=Europe/Kyiv
RUN apk add --no-cache tzdata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY . /app

CMD flask db migrate -m "Auto migration" && flask db upgrade && flask --app app.py run -h 0.0.0.0 -p $PORT
