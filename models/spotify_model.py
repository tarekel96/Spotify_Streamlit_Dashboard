import logging
import os
import requests
from dotenv import load_dotenv

class Spotify_Model:
    def __init__(self) -> None:
        load_dotenv()
        self.CLIENT_ID = os.environ.get('CLIENT_ID')
        self.CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
        self.SEARCH_CATEGORIES = ["album", "artist", "playlist", "track", "show", "episode", "audiobook"]
    
    def _gen_access_token(self):
        url = 'https://accounts.spotify.com/api/token'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {
            'grant_type': 'client_credentials',
            'client_id': self.CLIENT_ID,
            'client_secret': self.CLIENT_SECRET
        }
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()
        json_response = response.json()
        return json_response['access_token']
    
    def query(self, category: str, query: str):
        if category not in self.SEARCH_CATEGORIES:
            logging.error("ERROR: An invalid search category, {}, was provided.".format(category))
            return
        access_token = self._gen_access_token()
        url = 'https://api.spotify.com/v1/search'
        headers={ 'authorization': f'Bearer {access_token}'}
        params={ 'q': query, 'type': category }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def query_artists(self, query: str):
        access_token = self._gen_access_token()
        url = 'https://api.spotify.com/v1/search'
        headers={ 'authorization': f'Bearer {access_token}'}
        params={ 'q': query, 'type': 'artist' }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        response_items = response.json()['artists']['items']
        results = []
        for item in response_items:
            id, name, genres, popularity, followers, images = item['id'], item['name'], item['genres'], item['popularity'], item['followers']['total'], item['images']
            record = {
                'id': id,
                'name': name,
                'genres': genres,
                'popularity': popularity,
                'followers': followers,
                'images': images
            }
            results.append(record)
        return results