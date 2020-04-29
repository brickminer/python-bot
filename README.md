# Brickminer Bot

Lego information bot for Telegram writen in Python

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

Fill your database credentials and Telegram API token into your `.env` file.

## Running locally (Docker)

```bash
docker-compose -f docker-compose.yml -f docker-compose-dev.yml up -d
```

## Running in prod (Docker)

```bash
docker-compose up -d
```

## Running without Docker

```bash
python bot.py
```
