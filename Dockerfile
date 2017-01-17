FROM delr3ves/raspbian-python3:0.0.1
ENV PYTHONUNBUFFERED 1
WORKDIR /code
ADD . /code/
ADD ./atalaya_server/rpi_settings.py /code/atalaya_server/custom_settings.py

RUN pip3 install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]