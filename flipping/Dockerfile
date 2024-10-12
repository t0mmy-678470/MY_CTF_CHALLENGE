FROM python:3-slim

RUN apt-get update -y && \
    apt-get install socat -y && \
    pip install pycryptodome

COPY chall.py /app/chall.py

EXPOSE 10001

ENTRYPOINT socat TCP4-LISTEN:10001,tcpwrap=script,reuseaddr,fork EXEC:"/usr/bin/env python3 -u /app/chall.py"
