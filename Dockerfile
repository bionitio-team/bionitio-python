FROM python:3.7.3-stretch
WORKDIR /tmp/bionitio
COPY . .
RUN pip3 install .
ENTRYPOINT ["bionitio"]
