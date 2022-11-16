from time import sleep
from pathlib import Path
from os import environ
from dotenv import load_dotenv
import psycopg2
import logging

logger = logging.getLogger(__name__)

load_dotenv()

POSTGRES_URL = environ["POSTGRES_URL"]
POSTGRES_PORT = environ["POSTGRES_PORT"]
POSTGRES_DB = environ["POSTGRES_DB"]
POSTGRES_USER = environ["POSTGRES_USER"]
POSTGRES_PASSWORD = environ["POSTGRES_PASSWORD"]


def connect_db():
    while True:
        try:
            logger.info('Trying to connect to DB.')
            connection = psycopg2.connect(user=POSTGRES_USER,
                                          password=POSTGRES_PASSWORD,
                                          host=POSTGRES_URL,
                                          port=POSTGRES_PORT,
                                          database=POSTGRES_DB,
                                          connect_timeout=1)
            logger.info('Connection to DB was successful.')
            return connection
        except psycopg2.OperationalError as error:
            logger.error(f'Cannot connect to database. Trying again in 10 seconds.\n{str(error)}')
            sleep(10)


if __name__ == '__main__':
    # import logging.config
    # current_path = Path(__file__).parent.absolute()
    # logging.config.fileConfig(fr'{current_path}\...\logging.conf')
    connect_db()
