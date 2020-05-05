# Brickminer Bot

Lego information bot for Telegram writen in Python.

## Pre Requistes

- Python 3
- virtualenv
- Mysql
- docker / docker-compose (Optional)

## Setup

```bash
virtualenv bot-env
source bot-env/bin/activate
pip install -r requirements.txt
```

Rename your `.env.dist` to `.env`

```bash
mv `.env.dist` `.env`
```

Fill your database credentials and Telegram API token into your `.env` file. All configurations are read from this file.

## Running locally (Docker)

```bash
docker-compose -f docker-compose.yml
```

## Running in prod (Docker)

```bash
docker-compose up -d
```

## Running with localenv

```bash
python bot.py
```

## Development

This small application was created using VSCode as IDE. I would suggest this [video](https://www.youtube.com/watch?v=W--_EOzdTHk) teaching how to setup a development environment properly

## Preparing Database

By default, the bot is configured to get data dom SQLITE, but you can configure basicaly any database compatible with SQLAlchemy library. To change database, you need to update your `.env` file with a proper connection string

SQLite
```bash
DB_CONNECTION=sqlite:///data/sample.db
```

Mysql
```bash
DB_CONNECTION=mysql+mysqldb://user:pass@localhost:3306/db
```

### Creating database

In case you don't have a database created, you can execute the following commands
```bash
python cli.py -c create-tables
```

To Drop tables, execute:
```bash
python cli.py -c create-tables
```

You can find a sample SQLite database in `data/sample.db`

## Tests
To execute unit tests, just run

```bash
pytest
```
