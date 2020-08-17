from confluencli.util import log, handler
from confluencli import __version__

logger = log.get_logger()
error_type = handler.ErrorType


class Version():
    def show(self):
        print(__version__.__version__)
