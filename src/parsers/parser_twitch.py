import requests
from src.config.config import twitch_config


class TwitchParser:
    def __init__(self):
        self.streams = twitch_config.streams
        self.client_id = twitch_config.client_id
        self.auth_url = twitch_config.auth_url
        self.client_secret = twitch_config.client_secret

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
