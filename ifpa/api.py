import logging

logger = logging.getLogger(__name__)
from .base import _get
from .base import URL
from . import *


class IfpaApi():

    def __init__(self, api_key, default_raw=False):
        self.api_key = api_key
        self.url = URL
        self.default_raw = default_raw

    def _get(self, endpoint, raw_response=None, params={}, *args, **kwargs):
        if raw_response == None:
            raw_response = self.default_raw

        return _get(self.api_key, endpoint, params, raw_response=raw_response, *args,
                    **kwargs)

    def calendar_history(self, country=None, request_params={}, *args, **kwargs):
        request_params['country'] = country
        return calendar_history(self.api_key, country=None, request_params=request_params, raw_response=None, *args,
                                **kwargs)

    def calendar(self, calendar_id, request_params={}, *args, **kwargs):

        return calendar(self.api_key, calendar_id, request_params=request_params, raw_response=None, *args, **kwargs)

    def calendar_search(self, address=None, m=None, k=None, request_params={}, *args, **kwargs):
        return calendar_search(self.api_key, address=None, m=None, raw_response=None, k=None, request_params={}, *args,
                               **kwargs)

    def player(self, player_id, request_params={}, *args, **kwargs):
        return player(self.api_key, player_id, request_params=request_params, raw_response=None, *args, **kwargs)

    def player_results(self, player_id, request_params={}, *args, **kwargs):
        return player_results(self.api_key, player_id, request_params=request_params, raw_response=None, *args,
                              **kwargs)

    def player_pvp(self, player_id, request_params={}, *args, **kwargs):
        return player_pvp(self.api_key, player_id, request_params=request_params, raw_response=None, *args, **kwargs)

    def player_search(self, q, email=None, request_params={}, *args, **kwargs):
        return player_search(self.api_key, q, email=email, raw_response=None, request_params=request_params, *args,
                             **kwargs)

    def player_country_directors(self, request_params={}, *args, **kwargs):
        return player_country_directors(self.api_key, request_params=request_params, raw_response=None, *args ** kwargs)

    def player_history(self, player_id, request_params={}, *args, **kwargs):
        return player_history(self.api_key, player_id, request_params=request_params, raw_response=None, *args,
                              **kwargs)

    def pvp(self, p1, p2, request_params={}, *args, **kwargs):
        return pvp(self.api_key, p1, p2, request_params=request_params, raw_response=None, *args, **kwargs)

    def rankings(self, start_pos=None, count=None, order=None, request_params={}, *args, **kwargs):
        raise Exception("NYI.  at some point")
        # return rankings(self.api_key, start_pos=None, count=None, raw_response=None, order=None, request_params={},
        #               *args, **kwargs)

    def stats_points_this_year(self, request_params={}, *args, **kwargs):
        return stats_points_this_year(self.api_key, request_params=request_params, raw_response=None, *args ** kwargs)

    def stats_most_events(self, request_params={}, *args, **kwargs):
        return stats_most_events(self.api_key, request_params=request_params, raw_response=None, *args ** kwargs)

    def stats_country_players(self, request_params={}, *args, **kwargs):
        return stats_country_players(self.api_key, request_params=request_params, raw_response=None, *args ** kwargs)

    def stats_events_by_year(self, request_params={}, *args, **kwargs):
        return stats_events_by_year(self.api_key, request_params=request_params, raw_response=None, *args ** kwargs)

    def stats_players_by_year(self, request_params={}, *args, **kwargs):
        return stats_players_by_year(self.api_key, request_params=request_params, raw_response=None, *args ** kwargs)

    def stats_biggest_movers(self, request_params={}, *args, **kwargs):
        return stats_biggest_movers(self.api_key, request_params=request_params, raw_response=None, *args ** kwargs)

    def tournament(self, tournament_id, request_params={}, *args, **kwargs):
        return tournament(self.api_key, tournament_id, request_params=request_params, raw_response=None, *args,
                          **kwargs)

    def tournament_results(self, tournament_id, event_id=None, tour_date=None, request_params={}, *args, **kwargs):
        return tournament_results(self.api_key, tournament_id, event_id=None, raw_response=None, tour_date=None,
                                  request_params={}, *args, **kwargs)

    def tournament_list(self, request_params={}, *args, **kwargs):
        return tournament_list(self.api_key, request_params=request_params, raw_response=None, *args ** kwargs)

    def tournament_search(self, q, request_params={}, *args, **kwargs):
        request_params['q'] = q
        return tournament_search(self.api_key, q, request_params=request_params, raw_response=None, *args, **kwargs)
