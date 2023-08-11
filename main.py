import logging
from models.spotify_model import Spotify_Model

def main():
    logging.basicConfig(level=logging.INFO)
    spotify = Spotify_Model()
    query_results = spotify.search(category='artist', query='Travis Scott')
    print(query_results)

if __name__ == '__main__':
    main()