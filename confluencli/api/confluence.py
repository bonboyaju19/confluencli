import requests
from confluencli.util import log, handler
from confluencli.model import base

logger = log.get_logger()
error_type = handler.ErrorType


class Confluence:
    def get_content(self, content_id):
        return self.__get(path="/rest/api/content/" + content_id, params={"expand": "ancestors,body.storage"})

    def get_content_child(self, content_id):
        return self.__get(path="/rest/api/content/" + content_id + "/child/page")

    def get_content_attachment(self, content_id):
        return self.__get(path="/rest/api/content/" + content_id + "/child/attachment")

    def get_content_label(self, content_id):
        return self.__get(path="/rest/api/content/" + content_id + "/label")

    def get_attachment_file(self, path):
        return self.__get_stream(path=path)

    def __get(self, path, auth=(base.Base().username, base.Base().password), params={}):
        response = requests.get(base.Base().base_url +
                                path, auth=auth, params=params)
        # logger.info("response code: " + str(response.status_code))
        if response.headers['content-type'] == "application/json":
            logger.info(response.json())
            return response.json()
        elif response.headers['content-type'] == "text/html":
            logger.info(response.text)
            return response.text
        else:
            logger.info(response.text)
            return response.content

    def __get_stream(self, path, auth=(base.Base().username, base.Base().password), params={}, chunk_size=1024*10):
        with requests.get(base.Base().base_url + path, auth=auth, params=params, stream=True) as r:
            r.raise_for_status()
            for chunk in r.iter_content(chunk_size=chunk_size):
                yield chunk
