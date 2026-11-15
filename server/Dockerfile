FROM python:3.15-slim-trixie

WORKDIR /work

RUN useradd --uid 10001 app

COPY server.py .

EXPOSE 8000
USER 10001

CMD ["python3", "server.py"]