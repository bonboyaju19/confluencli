from dataclasses import dataclass, field
from typing import List, Dict
from confluencli.util import log, handler
from confluencli.model import attachment, label


logger = log.get_logger()
error_type = handler.ErrorType


@dataclass
class Content:
    id: str = ""
    title: str = ""
    body: str = ""
    extension: str = ".html"
    parent_id: str = ""
    children_id: List[str] = field(default_factory=list)
    attachments: List[attachment.Attachment] = field(default_factory=list)
    labels: List[label.Label] = field(default_factory=list)

    def __post_init__(self):
        if not isinstance(self.id, str):
            # logger.info("conver " +
            #             type(self.id).__name__ + " to " + type(str).__name__)
            self.id = str(self.id)
