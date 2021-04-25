import os
from fastapi import FastAPI
from typing import Optional
from giantbomb_game_fetcher import GiantBombGameFetcher

tags_metadata = [
    {
        "name": "video_games",
        "description": "This is the base URL for the Rest API Interface"
    },
    {
        "name": "get_video_game_results",
        "description": "This is the endpoint to get the results from API, it returns 10 results",
        "externalDocs": {
            "description": "The Source API for our data",
            "url": "https://www.giantbomb.com/api/documentation/"
        }
    },
    {
        "name": "get_all_video_game_results",
        "description": "This is the endpoint to get the complete results from API, we paginate upto 10 pages "
                       "and return the results",
        "externalDocs": {
            "description": "The Source API for our data",
            "url": "https://www.giantbomb.com/api/documentation/"
        }
    }

]

app = FastAPI(
    title="Giant Bomb Games API",
    description="This is a simple API service that returns the Game information from Giantbomb API",
    version="1.0.0",
    openapi_tags=tags_metadata
)


api_key = os.getenv('GIANTBOMB_API_KEY')


@app.get("/", tags=["video_games"])
def read_root():
    return {"This is the API for Video Game Resources"}


@app.get("/games/{video_game}", tags=["get_video_game_results"])
def get_video_game(video_game: str = None, page: Optional[int] = 0):
    try:
        game_fetcher = GiantBombGameFetcher(api_key=api_key)
        if page:
            return game_fetcher.fetch_response(video_game, page)
        return game_fetcher.fetch_response(video_game)

    except Exception as e:
        print("Oops!", e.__class__, "occurred.")


@app.get("/games/{video_game}/all", tags=["get_all_video_game_results"])
def get_all_matching_video_games(video_game: str = None):
    try:
        game_fetcher = GiantBombGameFetcher(api_key=api_key)
        return game_fetcher.fetch_complete_response(video_game)

    except Exception as e:
        print("Oops!", e.__class__, "occurred.")

