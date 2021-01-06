import os
from confluencli.util import log, handler

logger = log.get_logger()
error_type = handler.ErrorType
env_type = handler.EnvType


def get_env_value_from(key):
    os.getenv(key)
    pass


def set_credential(base):
    if env_type.WIKI_USERNAME_ENV.value not in os.environ:
        handler.handle_error(error_type.CONFLUENCLI_USERNAME_NOT_EXIST)
    if env_type.WIKI_PASSWORD_ENV.value not in os.environ:
        handler.handle_error(error_type.CONFLUENCLI_PASSWORD_NOT_EXIST)
    base.username = os.getenv(env_type.WIKI_USERNAME_ENV.value)
    base.password = os.getenv(env_type.WIKI_PASSWORD_ENV.value)


def set_base_url(base):
    if env_type.WIKI_BASEURL_ENV.value not in os.environ:
        handler.handle_error(error_type.CONFLUENCLI_BASEURL_NOT_EXIST)
    base.base_url = os.getenv(env_type.WIKI_BASEURL_ENV.value).rstrip('/')
