#!/bin/sh
# wait-for-db.sh

set -e


until PGPASSWORD=$POSTGRES_PASSWORD psql -h "db" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
flask db migrate; flask db upgrade
flask --app app.py run -h 0.0.0.0 -p $PORT