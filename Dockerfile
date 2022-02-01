FROM python:3.10.2-slim-bullseye
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT [ "python" ]
CMD ["src/coins.py"]
