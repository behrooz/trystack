from python:slim

Label maintainer="behrooz razzaghi <razzaghi.b@gmail.com>"

ENV TRYSTACK_API_ENV=production TRYSTACK_API_DEBUG=0 SQLALCHEMY_DATABASE_URI=mysql+pymysql://root:123@192.168.2.65:3306/trystack

EXPOSE 5000/tcp

WORKDIR /opt/src

COPY requirment.txt .

RUN pip install -r requirment.txt

COPY . . 