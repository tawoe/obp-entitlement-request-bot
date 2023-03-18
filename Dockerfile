FROM python:slim
ADD . /app
RUN pip install -r /app/requirements.txt
CMD ["python", "main.py"]