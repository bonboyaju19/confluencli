from dataclasses import dataclass, field
from confluencli.util import log, handler
from confluencli.model import attachment
from confluencli.repository import base_repository

logger = log.get_logger()
error_type = handler.ErrorType


@dataclass
class AttachmentRepository(base_repository.BaseRepository):
    def get_attachments(self, content_id):
        attachments_response = self.confluence_api.get(
            path="/rest/api/content/" + content_id + "/child/attachment")
        attachments_list = []
        for ar in attachments_response["results"]:
            attachments_list.append(attachment.Attachment(
                id=ar["id"],
                title=ar["title"],
                media_type=ar["metadata"]["mediaType"],
                webui_url=ar["_links"]["webui"],
                download_url=ar["_links"]["download"])
            )
        return attachments_list

    def download_stream(self, attachment_):
        for data in self.confluence_api.get_stream(path=attachment_.download_url):
            yield data
