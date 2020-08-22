import zipstream
from dataclasses import dataclass, field
from confluencli.util import log, handler
from confluencli.model import content
from confluencli.repository import content_repository, label_repository, attachment_repository


logger = log.get_logger()
error_type = handler.ErrorType


@dataclass
class PageService:
    content_repo: content_repository.ContentRepository = field(
        default_factory=content_repository.ContentRepository
    )
    label_repo: label_repository.LabelRepository = field(
        default_factory=label_repository.LabelRepository
    )
    attachment_repo: attachment_repository.AttachmentRepository = field(
        default_factory=attachment_repository.AttachmentRepository
    )

    def set_page(self, content_):
        self.content_repo.set_content(content_)
        self.content_repo.set_content_children(content_)
        self.label_repo.set_label(content_)
        self.attachment_repo.set_attachment(content_)

    def archive_page(self, content_, current_path, zipfile, is_recursive):
        zipfile.writestr(
            current_path + "/" + content_.title + content_.extension,
            content_.body.encode('utf-8')
        )
        for attachment_ in content_.attachments:
            zipfile.write_iter(
                current_path + "/" + "attachments/" +
                attachment_.id + "_" + attachment_.title,
                self.attachment_repo.download_stream(attachment_)
            )
        if is_recursive:
            if not content_.children_id:
                current_path += "/.."
                return
            for child_id in content_.children_id:
                child = content.Content(id=child_id)
                self.content_repo.set_content(child)
                self.content_repo.set_content_children(child)
                self.attachment_repo.set_attachment(child)
                self.archive_page(
                    child,
                    current_path + "/" + child.id,
                    zipfile,
                    is_recursive
                )
