from dataclasses import dataclass
from confluencli.util import log, handler, config


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
        config.set_credential(self)
        config.set_base_url(self)
