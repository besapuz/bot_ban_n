from time import sleep
from pathlib import Path
from os import environ
from dotenv import load_dotenv
import logging

from ldap3.core.exceptions import LDAPSocketOpenError
from ldap3 import Connection, RESTARTABLE

logger = logging.getLogger(__name__)

load_dotenv()

LDAP_URL = environ["LDAP_URL"]
LDAP_LOGIN = environ["LDAP_LOGIN"]
LDAP_PASSWORD = environ["LDAP_PASSWORD"]


def connect_ad():
    try:
        logger.info('Trying to connect to Active Directory.')
        ldap = Connection(LDAP_URL, LDAP_LOGIN, LDAP_PASSWORD, auto_bind=True, client_strategy=RESTARTABLE)
        logger.info('Connection to Active Directory was established.')
        return ldap
    except LDAPSocketOpenError as e:
        logger.error('AD server is unavailable. Trying again in 10 seconds.')
        print(e)
        # sleep(10)
        # logger.info("Trying to connect to AD again.")
        # connect_ad()


if __name__ == '__main__':
    import logging.config
    current_path = Path(__file__).parent.absolute()
    logging.config.fileConfig(fr'{current_path}\..\logging.conf')
    connect_ad()
