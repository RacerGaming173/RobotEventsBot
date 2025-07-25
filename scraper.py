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

    def get_events_data(self):
        r = requests.get(vars.base_robotevents_url + '/events', params=self.params, headers=self.headers)
        raw_json = json.loads(r.text)
        return raw_json