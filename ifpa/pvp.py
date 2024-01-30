import logging

from .base import _get

logger = logging.getLogger(__name__)


def pvp(api_key, p1, p2, request_params={}, *args, **kwargs):
    """
    GET pvp

    Get player and tournament information.
    """

    url = f"""pvp"""
    return _get(api_key, url, params=request_params, *args, **kwargs)
