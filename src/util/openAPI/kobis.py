import requests

from src.core import settings


def get_movie_details(movie_cd):
    response = requests.get(
        url = settings.API_URL + '?' + \
            f'key={settings.API_KEY}' + '&' + \
                f'movieCD={movie_cd}'
    )
    
    movie_info = response['movieInfoResult']['movieInfo']
    
    genres = [ genre['genreNm'] for genre in movie_info['genres'] ]
    directors = [ director['peopleNm'] for director in movie_info['directors'] ]
    actors = [ actor['peopleNm'] for actor in movie_info['actors'] ]
    
    movie = {
        'nation': movie_info['nations']['nationNm'],
        'genres': genres,
        'director': directors,
        'actors': actors
    }
    
    return movie