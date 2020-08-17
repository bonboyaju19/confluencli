import os
import io
import zipstream
from confluencli.util import log, handler
from confluencli.model import content
from confluencli.repository import page_repository

logger = log.get_logger()
error_type = handler.ErrorType


class Page():
    def download(self, id, output="output.zip", recursive=True):
        _content = content.Content(id=id)
        page_repository.PageRepository().set_content(_content)
        z = zipstream.ZipFile()

        self.__archive(_content, "./" + _content.id, z, recursive)
        with open(output, "wb") as f:
            for data in z:
                f.write(data)

    def __archive(self, _content, current_path, zipfile, is_recursive):
        zipfile.writestr(
            current_path + "/" + _content.title + _content.extension,
            _content.body.encode('utf-8')
        )
        for _attachment in _content.attachments:
            zipfile.write_iter(
                current_path + "/" + "attachments/" +
                _attachment.id + "_" + _attachment.title,
                page_repository.PageRepository().download_stream(_attachment)
            )

        if is_recursive:
            if not _content.children_id:
                current_path += "/.."
                return
            for child_id in _content.children_id:
                _child = content.Content(id=child_id)
                page_repository.PageRepository().set_content(_child)
                self.__archive(
                    _child, current_path + "/" + _child.id, zipfile, is_recursive)
