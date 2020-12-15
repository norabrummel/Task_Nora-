FROM python:3 

WORKDIR /app/src

COPY task_nora.py . 

VOLUME /files

RUN pip3 install fpdf

CMD [ "python", "task_nora.py" ]