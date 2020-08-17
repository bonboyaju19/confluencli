import json
import os
from dataclasses import dataclass
from confluencli.util import log, handler
from confluencli.model import label, attachment
from confluencli.api import confluence

logger = log.get_logger()
error_type = handler.ErrorType


@dataclass
class PageRepository:
    def set_content(self, content):
        content_response = confluence.Confluence().get_content(content.id)
        content.title = content_response["title"]
        content.body = content_response["body"]["storage"]["value"]
        content.parent_id = content_response["ancestors"][0]["id"]

        children_response = confluence.Confluence().get_content_child(content.id)
        for cr in children_response["results"]:
            content.children_id.append(cr["id"])

        labels_response = confluence.Confluence().get_content_label(content.id)
        for lr in labels_response["results"]:
            content.labels.append(label.Label(
                id=lr["id"], name=lr["name"], label=lr["label"], content_id=content.id))

        attachments_response = confluence.Confluence().get_content_attachment(content.id)
        for ar in attachments_response["results"]:
            content.attachments.append(attachment.Attachment(
                id=ar["id"], title=ar["title"], media_type=ar["metadata"]["mediaType"], webui_url=ar["_links"]["webui"], download_url=ar["_links"]["download"]))

    def download_stream(self, attachment):
        for data in confluence.Confluence().get_attachment_file(attachment.download_url):
            yield data
