# pull official base image
FROM ubuntu:22.04

# create directory for the "kgf_admin" user
RUN mkdir -p /home/kgf_admin

# create the kgf_admin user
RUN addgroup --system kgf_admin && adduser --system kgf_admin --ingroup kgf_admin

# create the appropriate directories
ENV HOME=/home/kgf_admin
ENV APP_HOME=/home/kgf_admin/kyrgyz_go_database/source
RUN mkdir -p $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/uploads
WORKDIR $APP_HOME

# Set DEBIAN_FRONTEND to noninteractive to avoid prompts
ENV DEBIAN_FRONTEND noninteractive

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install primary dependencies (including psycopg2)
RUN apt-get update && apt-get install -y netcat
RUN apt-get update && apt-get install -y libpq5=14.7-0ubuntu0.22.04.1
RUN apt-get update && apt-get install -y build-essential python3 python3-dev python3-pip python3-virtualenv python3-setuptools gcc musl-dev postgresql postgresql-contrib vim

# install dependencies
RUN pip install --upgrade pip
COPY /requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY /entrypoint.sh .
RUN sed -i 's/\r$//g' $APP_HOME/entrypoint.sh
RUN chmod +x $APP_HOME/entrypoint.sh

# copy project
COPY . $APP_HOME

# chown all the files to the kgf_admin user
RUN chown -R kgf_admin:kgf_admin $APP_HOME

# change to the kgf_admin user
USER kgf_admin

# run entrypoint.sh
ENTRYPOINT ["/home/kgf_admin/kyrgyz_go_database/source/entrypoint.sh"]