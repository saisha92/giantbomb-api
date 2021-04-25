import requests


class GiantBombGameFetcher:

    def __init__(self, api_key):
        self.base_url = "https://www.giantbomb.com/api/search/"
        self.api_key = api_key,
        self.headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537."
                          "36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
        }
        self.keys = ['id', 'name', 'number_of_user_reviews', 'original_release_date', 'deck', 'date_added',
                     'date_last_updated', 'original_game_rating']

    def fetch_response(self, game_name: str, page: int = 0):
        payload = {"api_key": self.api_key, "query": game_name,
                   "format": "json", "resources": "game", "page": page}
        api_response = requests.request("GET", self.base_url, params=payload, headers=self.headers)
        response = api_response.json()
        api_result = [{key: d[key] for key in self.keys} for d in response['results']]
        return api_result

    def fetch_complete_response(self, game_name: str):
        payload = {"api_key": self.api_key, "query": game_name,
                   "format": "json", "resources": "game"}
        api_response = requests.request("GET", self.base_url, params=payload, headers=self.headers)
        response = api_response.json()
        total_results = response['number_of_total_results']
        total_pages = (total_results//10) if (total_results//10) < 10 else 10
        complete_api_response = [{key: data[key] for key in self.keys} for data in response['results']]
        for i in range(total_pages):
            page_result = self.fetch_response(game_name, i)
            complete_api_response = [*complete_api_response, *page_result]

        return complete_api_response
