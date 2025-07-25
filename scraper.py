import requests, datetime, json, vars

cur_time = datetime.datetime.now(datetime.timezone.utc)

class RetrieveEventData:
    params = {
    'start': cur_time,
    'per_page': 1,
    'event_type': 'tournament'
    }

    headers = {
    'Authorization': 'Bearer ' + vars.robotevents_api_key
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