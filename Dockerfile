from python:2.7

ADD ./ebay-python.py ebay-python.py
RUN easy_install ebaysdk
CMD ["python","ebay-python.py"]
