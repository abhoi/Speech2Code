import requests

# headers = {
#     # Request headers
#     "Ocp-Apim-Subscription-Key": "6a6728b9981d417280f4dad97f82df96",
#     "content-type": "application/json",
# }

# params ={
#     # Query parameter
#     # 'q': 'Create a function named getUser with arguments alpha, beta, and gamma which returns a list',
#     # Optional request parameters, set to default values
#     'timezoneOffset': '0',
#     'verbose': 'false',
#     'spellCheck': 'false',
#     'staging': 'false',
# }

class Speech2CodeRequest:
    def __init__(self, query, headers, params):
        self.query = query
        self.headers = headers
        self.params = params
        # self._create_request()

    def _create_request(self):
        try:
            self.params["q"] = self.query
            # r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/7cd5279c-2cdc-4234-b5dc-f2a4bfa809f2', headers=self.headers, params=self.params)
            r = requests.get("https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/7cd5279c-2cdc-4234-b5dc-f2a4bfa809f2", headers=self.headers, params=self.params)
            json = r.json()
            print(r.status_code)
            print(json)
            return json
            # print("Action/Intent", json['topScoringIntent']['intent'])
            # print("Entities", [ent['entity'] for ent in json['entities']])
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))