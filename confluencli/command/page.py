from dataclasses import dataclass, field
from confluencli.util import log, handler
from confluencli.model import content
from confluencli.service import download_page_service

logger = log.get_logger()
error_type = handler.ErrorType


@dataclass
class Page():
    download_page_srv: download_page_service.DownloadPageService = field(
        default_factory=download_page_service.DownloadPageService
    )

    def download(self, id, output="output.zip", recursive=False):
        self.download_page_srv.download(
            str(id),
            output,
            recursive
        )
