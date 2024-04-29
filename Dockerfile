# base image  
FROM python:3.10-slim-bookworm

# buat user dan working directory
ENV APP_HOME=/home/app/web
RUN mkdir -p $APP_HOME
RUN addgroup --system app && adduser --system --group app
WORKDIR $APP_HOME

RUN pip install --upgrade pip  

# copy dari work directory lokal ke work directory docker
COPY . $APP_HOME

# berikan akses ke non-root user
# RUN chown -R app:app $APP_HOME
# USER app

# install dependensi proyek
RUN pip install -r requirements.txt 

# ekspos port yang digunakan django 
EXPOSE 8000

# start server  
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--nothreading"]