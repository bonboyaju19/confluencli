import io
from dataclasses import dataclass, field
from typing import List
from confluencli.util import log, handler


logger = log.get_logger()
error_type = handler.ErrorType


@dataclass
class Attachment:
    id: str = ""
    title: str = ""
    content_id: str = ""
    media_type: str = ""
    extension: str = ""
    webui_url: str = ""
    download_url: str = ""
