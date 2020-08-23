from dataclasses import dataclass
from confluencli.util import log, handler
from confluencli.repository import base_repository
from confluencli.model import content


logger = log.get_logger()
error_type = handler.ErrorType


@dataclass
class ContentRepository(base_repository.BaseRepository):
    def get_content(self, content_id):
        content_response = self.confluence_api.get(
            path="/rest/api/content/" +
            content_id, params={"expand": "ancestors,body.storage"}
        )
        return content.Content(
            id=content_id,
            title=content_response["title"],
            body=content_response["body"]["storage"]["value"],
            parent_id=content_response["ancestors"][0]["id"]
        )

    def get_content_children(self, content_id):
        children_response = self.confluence_api.get(
            path="/rest/api/content/" + content_id + "/child/page")
        children_list = []
        for cr in children_response["results"]:
            children_list.append(cr["id"])
        return children_list
