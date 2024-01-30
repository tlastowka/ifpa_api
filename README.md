Python interface to the IFPA API

I had a bunch disorganized one off scripts I use to query the IFPA api a bunch of different ways that I was tired of keeping track of so I made a single client.


I then added every  api function currently listed in the documentation.

https://www.ifpapinball.com/api/documentation/



There's some undocumented functions within the API but they aren't in here.

There's also constant rumors API v2 is coming sometime between now and forever. 

I've tested enough for my own scripts but most of these functions haven't been tested yet.

USE AT YOUR OWN RISK.

If you find a bug let me know and I'll see about fixing it.

You can import and call individual functions or invoke the full client.
They return the same output.  Check the API docs to find out about all the functions.

via a client
```
from ifpa.api import IfpaApi
IFPA_API_KEY = "GET_YOUR_OWN_KEY"
api = IfpaApi(IFPA_API_KEY)
client_call = api.player(1)
print(client_call)

```

via a single function
```
from ifpa.player import player
IFPA_API_KEY = "GET_YOUR_OWN_KEY"
single_function = player(IFPA_API_KEY,1)
print(single_function)
```

Either will produce the same output.  Something like this:

```{'player': {'age': 52,
            'city': 'Carlsbad',
            'country_code': 'US',
            'country_name': 'United States',
            'excluded_flag': 'N',
            'first_name': 'Keith',
            'gender': 'male',
            'ifpa_registered': 'Y',
            'initials': 'KME',
            'last_name': 'Elwin',
            'player_id': '1',
            'state': 'CA'},
 'player_stats': {'average_finish': '6',
                  'average_finish_last_year': '11',
                  'best_finish': '1',
                  'best_finish_count': '87',
                  'current_wppr_rank': '19',
                  'current_wppr_value': '1410.42',
                  'efficiency_rank': '95',
                  'efficiency_value': '60.520',
                  'highest_rank': '1',
                  'highest_rank_date': '2017-04-01',
                  'last_month_rank': '18',
                  'last_year_rank': '25',
                  'ratings_rank': '7',
                  'ratings_value': '1988.32',
                  'total_active_events': '24',
                  'total_events_all_time': '290',
                  'total_events_away': '4',
                  'wppr_points_all_time': '9563.98'}}
{'player': {'player_id': '1', 'first_name': 'Keith', 'last_name': 'Elwin', 'gender': 'male', 'city': 'Carlsbad', 'state': 'CA', 'country_code': 'US', 'country_name': 'United States', 'initials': 'KME', 'age': 52, 'excluded_flag': 'N', 'ifpa_registered': 'Y'}, 'player_stats': {'current_wppr_rank': '19', 'last_month_rank': '18', 'last_year_rank': '25', 'highest_rank': '1', 'highest_rank_date': '2017-04-01', 'current_wppr_value': '1410.42', 'wppr_points_all_time': '9563.98', 'best_finish': '1', 'best_finish_count': '87', 'average_finish': '6', 'average_finish_last_year': '11', 'total_events_all_time': '290', 'total_active_events': '24', 'total_events_away': '4', 'ratings_rank': '7', 'ratings_value': '1988.32', 'efficiency_rank': '95', 'efficiency_value': '60.520'}}
```
