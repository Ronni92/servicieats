FROM python:3.10

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x start.sh

EXPOSE 5001

CMD ["./start.sh"]
