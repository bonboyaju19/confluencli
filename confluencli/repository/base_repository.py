from dataclasses import dataclass, field
from confluencli.util import log, handler
from confluencli.model import attachment
from confluencli.api import confluence

logger = log.get_logger()
error_type = handler.ErrorType


@dataclass
class BaseRepository:
    confluence_api: confluence.ConfluenceApi = field(
        default_factory=confluence.ConfluenceApi
    )
