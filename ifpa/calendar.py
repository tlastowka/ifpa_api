import logging

from .base import _get

logger = logging.getLogger(__name__)


def calendar_active(api_key, country=None, request_params={}, *args, **kwargs):
    """
    GET calendar/active

    Get a list of current calendar entries.
    """

    url = f"""calendar/active"""
    return _get(api_key, url, params=request_params, *args, **kwargs)


def calendar_history(api_key, country=None, request_params={}, *args, **kwargs):
    """
    GET calendar/history

    Get a list of past calendar entries.
    """

    url = f"""calendar/history"""
    return _get(api_key, url, params=request_params, *args, **kwargs)


def calendar(api_key, calendar_id, request_params={}, *args, **kwargs):
    """
    GET calendar/{calendar_id}

    Get data regarding a specific calendar entry.
    """

    url = f"""calendar/{calendar_id}"""
    return _get(api_key, url, params=request_params, *args, **kwargs)


def calendar_search(api_key, address=None, m=None, k=None, request_params={}, *args, **kwargs):
    """
    GET calendar/search

    Search for specific calendar entries.
    """

    url = f"""calendar/search"""
    return _get(api_key, url, params=request_params, *args, **kwargs)
