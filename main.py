import logging
from models.spotify_model import Spotify_Model

def main():
    logging.basicConfig(level=logging.INFO)
    spotify = Spotify_Model()
    print(spotify.gen_access_token())

if __name__ == '__main__':
    main()