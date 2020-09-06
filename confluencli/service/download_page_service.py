import zipstream
from dataclasses import dataclass, field
from confluencli.util import log, handler
from confluencli.model import content
from confluencli.repository import content_repository, label_repository, attachment_repository


logger = log.get_logger()
error_type = handler.ErrorType


@dataclass
class DownloadPageService:
    content_repo: content_repository.ContentRepository = field(
        default_factory=content_repository.ContentRepository
    )
    label_repo: label_repository.LabelRepository = field(
        default_factory=label_repository.LabelRepository
    )
    attachment_repo: attachment_repository.AttachmentRepository = field(
        default_factory=attachment_repository.AttachmentRepository
    )

    def download(self, content_id, output, is_recursive):
        page_ = self.get(content_id)
        z = zipstream.ZipFile()
        self.archive(
            page_,
            "./" + page_.id,
            z,
            is_recursive
        )
        with open(output, "wb") as f:
            for data in z:
                f.write(data)

    def get(self, content_id):
        page_ = self.content_repo.get(content_id)
        page_.children_id = self.content_repo.get_children(
            content_id)
        page_.attachments = self.attachment_repo.get_list(
            content_id)
        page_.labels = self.label_repo.get_list(content_id)
        return page_

    def archive(self, content_, current_path, zipfile, is_recursive):
        zipfile.writestr(
            current_path + "/" + content_.title + content_.extension,
            content_.body.encode('utf-8')
        )
        for attachment_ in content_.attachments:
            zipfile.write_iter(
                current_path + "/attachments/" +
                attachment_.id + "_" + attachment_.title,
                self.attachment_repo.download_stream(attachment_)
            )
        if is_recursive:
            if not content_.children_id:
                current_path += "/.."
                return
            for child_id in content_.children_id:
                child = content.Content(id=child_id)
                child = self.content_repo.get(child.id)
                child.children_id = self.content_repo.get_children(
                    child.id)
                child.attachments = self.attachment_repo.get_list(
                    child.id)
                child.labels = self.label_repo.get_list(
                    child.id
                )
                self.archive(
                    child,
                    current_path + "/" + child.id,
                    zipfile,
                    is_recursive
                )
