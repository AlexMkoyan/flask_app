FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip3 install Flask
EXPOSE 3000
# ENV enviroment=dev
ARG MODE=--dev
CMD ["python3","./index.py","${MODE}","1"]

# docker build -t flask_docker .
# docker run -d -p 3000:3000 flask_docker
# docker build -t flask_docker --build-arg MODE=--prod .