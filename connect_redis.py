import redis
import logging
from os import environ
from dotenv import load_dotenv
from time import sleep
from pathlib import Path

logger = logging.getLogger(__name__)

load_dotenv()

REDIS_DB_URL = environ["REDIS_DB_URL"]
REDIS_DB_PORT = int(environ["REDIS_DB_PORT"])


def connect_redis():
    try:
        connection = redis.StrictRedis(host=REDIS_DB_URL,
                                       port=REDIS_DB_PORT,
                                       db=7,
                                       charset="utf-8",
                                       decode_responses=True)

        return connection
    except redis.ConnectionError as error:
        logger.error(f'Cannot connect to redis. Trying again in 10 seconds.\n{str(error)}')
        sleep(10)
        logger.info("Trying to connect to redis again.")
        connect_redis()


if __name__ == '__main__':
    import logging.config
    current_path = Path(__file__).parent.absolute()
    logging.config.fileConfig(fr'{current_path}\..\logging.conf')
    connect_redis()