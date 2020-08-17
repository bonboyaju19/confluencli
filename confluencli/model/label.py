from dataclasses import dataclass
from typing import List
from confluencli.util import log
from confluencli.util import handler


logger = log.get_logger()
error_type = handler.ErrorType


@dataclass
class Label:
    id: str = ""
    name: str = ""
    label: str = ""
    content_id: str = ""
