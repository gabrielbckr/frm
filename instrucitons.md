# Instructions

### Running Server
```
python -m frm
```

### Postgres

Install  dependencies:
```
sudo apt install psycopg2
```
Run docker exposing ports and setting volume storage

``` shell
docker-compose up
```

## Shell command:

### mariadb
```
docker run --rm --name mariadb -e MYSQL_ROOT_PASSWORD=docker \
-d -p 8080:7020 \
-v $HOME/docker/volumes/mysql:/var/lib/mysql/  mariadb
```
### postgres
```
docker run --name frm-psql \
    -e POSTGRES_PASSWORD=pass \
    -e POSTGRES_USER=usr \
    -e POSTGRES_DB=sqlalchemy \
    -p 5432:5432 \
    -d postgres
```


