#!/bin/sh
# wait-for-db.sh

set -e

until flask db migrate || flask db upgrade; do
  >&2 echo "Postgres is unavailable or migration failed - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
flask --app app.py run -h 0.0.0.0 -p $PORT
