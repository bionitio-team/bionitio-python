FROM python:3.7.3-stretch
WORKDIR /bionitio
COPY . .
RUN pip3 install .
RUN pip3 install -r requirements-dev.txt
ENTRYPOINT ["bionitio"]
