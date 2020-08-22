import zipstream
from dataclasses import dataclass, field
from confluencli.util import log, handler
from confluencli.model import content
from confluencli.service import page_service

logger = log.get_logger()
error_type = handler.ErrorType


@dataclass
class Page():
    page_srv: page_service.PageService = field(
        default_factory=page_service.PageService
    )

    def download(self, id, output="output.zip", recursive=False):
        content_ = content.Content(id=id)
        self.page_srv.set_page(content_)

        z = zipstream.ZipFile()
        self.page_srv.archive_page(content_, "./" + content_.id, z, recursive)
        with open(output, "wb") as f:
            for data in z:
                f.write(data)
