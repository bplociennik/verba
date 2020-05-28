#!/bin/sh

set -e

MANAGE_CMD='python src/manage.py'
SERVER_HOST='0.0.0.0:8000'
WAIT_FOR_DB='./compose/wait-for-it.sh postgres:5432 --'

if [ "$1" = 'manage' ]; then
  shift
  exec ${WAIT_FOR_DB} ${MANAGE_CMD} $@
elif [ "$1" = 'runserver' ]; then
  shift
  exec ${WAIT_FOR_DB} ${MANAGE_CMD} runserver ${SERVER_HOST} $@
elif [ "$1" = 'runserver_plus' ]; then
  shift
  exec ${WAIT_FOR_DB} ${MANAGE_CMD} runserver_plus ${SERVER_HOST} $@
elif [ "$1" = 'celery' ]; then
  shift
  exec ${WAIT_FOR_DB} celery -A config worker $@
elif [ "$1" = 'celery_beat' ]; then
  shift
  exec ${WAIT_FOR_DB} celery -A config beat $@
fi

exec "$@"
