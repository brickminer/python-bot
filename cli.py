import click
from bot.database import models


@click.command()
@click.option('-command', '-c')
def main(command):
    if command == 'create-tables':
        models.create_tables()
        return
    if command == 'drop-tables':
        models.drop_tables()
        return


if __name__ == "__main__":
    main()
