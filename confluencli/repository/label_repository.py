from dataclasses import dataclass
from confluencli.util import log, handler
from confluencli.model import label
from confluencli.repository import base_repository


logger = log.get_logger()
error_type = handler.ErrorType


@dataclass
class LabelRepository(base_repository.BaseRepository):
    def get_list(self, content_id):
        labels_response = self.confluence_api.get(
            path="/rest/api/content/" + content_id + "/label")
        labels_list = []
        for lr in labels_response["results"]:
            labels_list.append(label.Label(
                id=lr["id"],
                name=lr["name"],
                label=lr["label"],
                content_id=content_id)
            )
        return labels_list
