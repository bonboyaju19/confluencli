from dataclasses import dataclass
from confluencli.util import log, handler
from confluencli.model import label
from confluencli.repository import base_repository


logger = log.get_logger()
error_type = handler.ErrorType


@dataclass
class LabelRepository(base_repository.BaseRepository):
    def set_label(self, content):
        labels_response = self.confluence_api.get(
            path="/rest/api/content/" + content.id + "/label")
        for lr in labels_response["results"]:
            content.labels.append(label.Label(
                id=lr["id"], name=lr["name"], label=lr["label"], content_id=content.id))
