import os
import requests
from dotenv import load_dotenv

class Spotify_Model:
    def __init__(self) -> None:
        load_dotenv()
        self.CLIENT_ID = os.environ.get('CLIENT_ID')
        self.CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    
    def gen_access_token(self):
        url = 'https://accounts.spotify.com/api/token'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        # client_credentials&client_id=your-client-id&client_secret=your-client-secret
        payload = {
            'grant_type': 'client_credentials',
            'client_id': self.CLIENT_ID,
            'client_secret': self.CLIENT_SECRET
        }
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()
        print(response.status_code)
        json_response = response.json()
        print(json_response)
        return json_response['access_token']