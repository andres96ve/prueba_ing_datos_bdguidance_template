FROM postgres:13-alpine

ENV POSTGRES_DB dvdrental
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD 12345

ENV LANG ja_JP.utf8

COPY dvdrental.tar /tmp/dvdrental.tar
COPY 00_init.sql /docker-entrypoint-initdb.d/00_init.sql
COPY restore_db.sh /docker-entrypoint-initdb.d/restore_db.sh