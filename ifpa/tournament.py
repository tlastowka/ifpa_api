import logging

from .base import _get

logger = logging.getLogger(__name__)


def tournament(api_key, tournament_id, request_params={}, *args, **kwargs):
    """
    GET tournament/{tournament_id}

    Get information about a tournament.
    """

    url = f"""tournament/{tournament_id}"""
    return _get(api_key, url, params=request_params, *args, **kwargs)


def tournament_results(api_key, tournament_id, event_id=None, tour_date=None, request_params={}, *args, **kwargs):
    """
    GET tournament/{tournament_id}/results

    Get results for a tournament.
    """

    url = f"""tournament/{tournament_id}/results"""
    return _get(api_key, url, params=request_params, *args, **kwargs)


def tournament_list(api_key, request_params={}, *args, **kwargs):
    """
    GET tournament/list

    Get a highlevel list of tournaments.
    """

    url = f"""tournament/list"""
    return _get(api_key, url, params=request_params, *args, **kwargs)


def tournament_search(api_key, q, request_params={}, *args, **kwargs):
    """
    GET tournament/search

    Search for a tournament by name.
    """

    url = f"""tournament/search"""
    return _get(api_key, url, params=request_params, *args, **kwargs)
