import requests
from confluencli.util import log, handler
from confluencli.model import base

logger = log.get_logger()
error_type = handler.ErrorType


class ConfluenceApi:
    def get(self, path, auth=(base.Base().username, base.Base().password), params={}):
        response = requests.get(base.Base().base_url +
                                path, auth=auth, params=params)
        if response.headers['content-type'] == "application/json":
            logger.info(response.json())
            return response.json()
        elif response.headers['content-type'] == "text/html":
            logger.info(response.text)
            return response.text
        else:
            logger.info(response.text)
            return response.content

    def get_stream(self, path, auth=(base.Base().username, base.Base().password), params={}, chunk_size=1024*10):
        with requests.get(base.Base().base_url + path, auth=auth, params=params, stream=True) as r:
            r.raise_for_status()
            for chunk in r.iter_content(chunk_size=chunk_size):
                yield chunk
