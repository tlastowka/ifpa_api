import logging

from .base import _get

logger = logging.getLogger(__name__)


def stats_points_this_year(api_key, request_params={}, *args, **kwargs):
    """
    GET stats/points_this_year

    List of players who have earned the most points this year.
    """

    url = f"""stats/points_this_year"""
    return _get(api_key, url, params=request_params, *args, **kwargs)


def stats_most_events(api_key, request_params={}, *args, **kwargs):
    """
    GET stats/most_events

    List of players who have played in the most events the 3 years.
    """

    url = f"""stats/most_events"""
    return _get(api_key, url, params=request_params, *args, **kwargs)


def stats_country_players(api_key, request_params={}, *args, **kwargs):
    """
    GET stats/country_players

    Aggregate count of players by country.
    """

    url = f"""stats/country_players"""
    return _get(api_key, url, params=request_params, *args, **kwargs)


def stats_events_by_year(api_key, request_params={}, *args, **kwargs):
    """
    GET stats/events_by_year

    Aggregate Event count, by year.
    """

    url = f"""stats/events_by_year"""
    return _get(api_key, url, params=request_params, *args, **kwargs)


def stats_players_by_year(api_key, request_params={}, *args, **kwargs):
    """
    GET stats/players_by_year

    Aggregate Players by Year.
    """

    url = f"""stats/players_by_year"""
    return _get(api_key, url, params=request_params, *args, **kwargs)


def stats_biggest_movers(api_key, request_params={}, *args, **kwargs):
    """
    GET stats/biggest_movers

    Players who have moved the most positions since the beginning of the year (top 250).
    """

    url = f"""stats/biggest_movers"""
    return _get(api_key, url, params=request_params, *args, **kwargs)
