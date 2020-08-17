import fire
from confluencli.util import log, handler
from confluencli.command import page, version


logger = log.get_logger()
error_type = handler.ErrorType


class Cli:
    def __init__(self):
        self.page = page.Page()
        self.version = version.Version()

    def page(self):
        self.page

    def version(self):
        self.version
