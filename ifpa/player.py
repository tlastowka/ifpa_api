import logging

from .base import _get

logger = logging.getLogger(__name__)


def player(api_key, player_id, request_params={}, *args, **kwargs):
    """
    GET player/{player_id}

    Get information about a player.
    """

    url = f"""player/{player_id}"""
    return _get(api_key, url, params=request_params, *args, **kwargs)


def player_results(api_key, player_id, request_params={}, *args, **kwargs):
    """
    GET player/{player_id}/results

    Get tournament results for a player.
    """

    url = f"""player/{player_id}/results"""
    return _get(api_key, url, params=request_params, *args, **kwargs)


def player_pvp(api_key, player_id, request_params={}, *args, **kwargs):
    """
    GET player/{player_id}/pvp

    Get player comparisons for a specific player, at a high level. Note that
					this only brings back data if the player has played someone more than twice.
    """

    url = f"""player/{player_id}/pvp"""
    return _get(api_key, url, params=request_params, *args, **kwargs)


def player_search(api_key, q, email=None, request_params={}, *args, **kwargs):
    """
    GET player/search

    Search for players by either name or email.
    """

    url = f"""player/search"""
    return _get(api_key, url, params=request_params, *args, **kwargs)


def player_country_directors(api_key, request_params={}, *args, **kwargs):
    """
    GET player/country_directors

    Get a list of country directors.
    """

    url = f"""player/country_directors"""
    return _get(api_key, url, params=request_params, *args, **kwargs)


def player_history(api_key, player_id, request_params={}, *args, **kwargs):
    """
    GET player/{player_id}/history

    Get ranking and rating history for a player.
    """

    url = f"""player/{player_id}/history"""
    return _get(api_key, url, params=request_params, *args, **kwargs)
