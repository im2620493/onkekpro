FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
EXPOSE 8001
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
RUN chmod +x start.sh
