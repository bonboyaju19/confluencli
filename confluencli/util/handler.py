from confluencli.util import log
from enum import Enum
import sys

logger = log.get_logger()


class ErrorType(Enum):
    '''
    Naming Convention
    [MODULE NAME]_[ERROR OVERVIEW]
    '''

    CONFLUENCLI_USERNAME_NOT_EXIST = "Environent value 'WIKI_USERNAME' does not exist."
    CONFLUENCLI_PASSWORD_NOT_EXIST = "Environent value 'WIKI_PASSWORD' does not exist."
    CONFLUENCLI_BASEURL_NOT_EXIST = "Environent value 'WIKI_URL' does not exist."


class EnvType(Enum):
    '''
    Environment Value Type
    '''

    WIKI_USERNAME_ENV = "WIKI_USERNAME"
    WIKI_PASSWORD_ENV = "WIKI_PASSWORD"
    WIKI_BASEURL_ENV = "WIKI_URL"


def handle_error(error_type, exception=None, message=None):
    logger.error("%s:%s" % (error_type.name, error_type.value))
    sys.exit(1)
