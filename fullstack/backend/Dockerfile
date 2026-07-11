FROM python:3.12

WORKDIR /app

COPY requirement.txt .

RUN pip install --no-cache-dir -r requirement.txt

COPY . .

COPY start.sh .

RUN chmod +x start.sh

CMD ["/app/start.sh"]