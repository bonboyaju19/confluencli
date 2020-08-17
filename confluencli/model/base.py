import os
from dataclasses import dataclass
from confluencli.util import log, handler


logger = log.get_logger()
error_type = handler.ErrorType
env_type = handler.EnvType


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


@dataclass
class Base(metaclass=Singleton):
    username: str = ""
    password: str = ""
    base_url: str = ""

    def __post_init__(self):
        self.__set_credential()
        self.__set_base_url()

    def __set_credential(self):
        if env_type.WIKI_USERNAME_ENV.value not in os.environ:
            handler.handle_error(error_type.CONFLUENCLI_USERNAME_NOT_EXIST)
        if env_type.WIKI_PASSWORD_ENV.value not in os.environ:
            handler.handle_error(error_type.CONFLUENCLI_PASSWORD_NOT_EXIST)
        self.username = os.getenv(env_type.WIKI_USERNAME_ENV.value)
        self.password = os.getenv(env_type.WIKI_PASSWORD_ENV.value)

    def __set_base_url(self):
        if env_type.WIKI_BASEURL_ENV.value not in os.environ:
            handler.handle_error(error_type.CONFLUENCLI_BASEURL_NOT_EXIST)
        self.base_url = os.getenv(env_type.WIKI_BASEURL_ENV.value).rstrip('/')
