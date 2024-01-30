import logging

from .base import _get

logger = logging.getLogger(__name__)


def rankings(api_key, start_pos=None, count=None, order=None, request_params={}, *args, **kwargs):
    """
    GET rankings

    Get the WPPR rankings.
    """

    url = f"""rankings"""
    return _get(api_key, url, params=request_params, *args, **kwargs)
