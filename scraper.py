import requests, datetime, json, vars

class RetrieveEventData:
    headers = {
    'Authorization': 'Bearer ' + vars.robotevents_api_key
    }

    def __init__(self):
        self.cur_time = datetime.datetime.now(datetime.timezone.utc)

        self.params = {
        'start': self.cur_time,
        'per_page': 250,
        'event_type': 'tournament'
        }


    def set_query_param(self, key, val):
        self.params[key] = val

    def clear_query_param(self, key):
        if key in self.params:
            del self.params[key]

    def get_events_data(self):
        r = requests.get(vars.base_robotevents_url + '/events', params=self.params, headers=self.headers)
        raw_json = json.loads(r.text)
        return raw_json
    
    def update_current_time(self):
        self.cur_time = datetime.datetime.now(datetime.timezone.utc)