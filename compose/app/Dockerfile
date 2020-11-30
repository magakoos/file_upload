FROM python:3.8

# USR_LOCAL_BIN - путь до пользовательских скриптов
# PROJECT_ROOT - путь до каталога внутри контейнера, в который будет
# копироваться приложение
ENV USR_LOCAL_BIN=/usr/local/bin/  \
    PROJECT_ROOT=/app

## путь до исходников
ENV PYTHONPATH=$PYTHONPATH:$PROJECT_ROOT

# Создание директорий
RUN mkdir $PROJECT_ROOT/ && \
    mkdir $PROJECT_ROOT/run && \
    mkdir $PROJECT_ROOT/wsgi

COPY ./Pipfile ./Pipfile.lock $PROJECT_ROOT/
WORKDIR $PROJECT_ROOT

# Установка зависимостей
RUN pip install --upgrade wheel pip pipenv==2018.11.26 \
    && pipenv install --deploy --system --dev

# копирование непосредственно проекта
COPY ./src $PROJECT_ROOT

COPY ./compose/app/start_uwsgi $USR_LOCAL_BIN/

RUN sed -i 's/\r//' $USR_LOCAL_BIN/start_uwsgi \
    && chmod +x $USR_LOCAL_BIN/start_uwsgi

COPY ./compose/app/uwsgi.ini $PROJECT_ROOT/wsgi

EXPOSE 8000

CMD ["start_uwsgi"]
