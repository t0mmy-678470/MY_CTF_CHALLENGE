FROM python:3-slim

RUN apt-get update -y && \
    apt-get install socat -y

COPY chall.py /app/chall.py

EXPOSE 10000

ENTRYPOINT socat TCP4-LISTEN:10000,tcpwrap=script,reuseaddr,fork EXEC:"/usr/bin/env python3 -u /app/chall.py"
