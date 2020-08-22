from dataclasses import dataclass
from confluencli.util import log, handler
from confluencli.repository import base_repository


logger = log.get_logger()
error_type = handler.ErrorType


@dataclass
class ContentRepository(base_repository.BaseRepository):
    def set_content(self, content):
        content_response = self.confluence_api.get(
            path="/rest/api/content/" +
            content.id, params={"expand": "ancestors,body.storage"}
        )
        content.title = content_response["title"]
        content.body = content_response["body"]["storage"]["value"]
        content.parent_id = content_response["ancestors"][0]["id"]

    def set_content_children(self, content):
        children_response = self.confluence_api.get(
            path="/rest/api/content/" + content.id + "/child/page")
        for cr in children_response["results"]:
            content.children_id.append(cr["id"])
