import logging

import requests

logger = logging.getLogger(__name__)
URL = """https://api.ifpapinball.com/v1"""


def _get(api_key, endpoint, url=URL, params={}, raw_request=False, acceptable_returns=[200],  **kwargs):
    _params = {
        "api_key": api_key,
        **params,
        **kwargs
    }

    url = f"""{url}/{endpoint}"""

    logger.debug(f'get {endpoint = } {url = } {params = }')
    resp = requests.get(url, _params)
    if raw_request:
        return resp
    else:
        if resp.status_code not in acceptable_returns:
            raise Exception(f"response code {resp.status_code} not in [{','.join([str(a) for a in acceptable_returns])}]")

        return resp.json()

