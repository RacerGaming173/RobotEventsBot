import requests, datetime, json
from vars import ROBOTEVENTS_API_KEY, BASE_ROBOTEVENTS_URL

class RetrieveEventData:

    headers = {
    'Authorization': 'Bearer ' + ROBOTEVENTS_API_KEY
    }

    def __init__(self):
        self.cur_time = datetime.datetime.now(datetime.timezone.utc)

        self.params = {
        'start': self.cur_time,
        'per_page': 250,
        'event_type': 'tournament',
        'season': 197
        }


    def set_query_param(self, key, val):
        self.params[key] = val

    def clear_query_param(self, key):
        if key in self.params:
            del self.params[key]

    def get_events_data(self):
        r = requests.get(BASE_ROBOTEVENTS_URL + '/events', params=self.params, headers=self.headers)
        raw_json = json.loads(r.text)
        return raw_json
    
    def update_current_time(self):
        self.cur_time = datetime.datetime.now(datetime.timezone.utc)