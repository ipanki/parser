import requests
from src.config.config import config


class TwitchParser:
    def __init__(self):
        self.streams = config.STREAMS
        self.client_id = config.CLIENT_ID
        self.auth_url = config.AUTH_URL
        self.client_secret = config.CLIENT_SECRET

    def _get_data_twitch(self):
        response = requests.post(
            f"{self.auth_url}"
            f"?client_id={self.client_id}"
            f"&client_secret={self.client_secret}"
            f"&grant_type=client_credentials"
        )
        data = requests.get(
            self.streams,
            headers={
                "Authorization": f'Bearer {response.json()["access_token"]}',
                "Client-Id": self.client_id,
            },
        )
        return data

    def parse_twitch(self):
        stream_data = []
        data = self._get_data_twitch()

        for stream in data.json()['data']:
            data_twtich = {
                "game": stream["game_name"],
                "title": stream["title"],
                "type": stream["type"],
                "user_login": stream["user_login"],
                "user_name": stream["user_name"],
                "viewer_count": stream["viewer_count"],
            }
            stream_data.append(data_twtich)
        return stream_data
