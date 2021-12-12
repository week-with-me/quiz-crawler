import json
import requests

from src.core import settings


def get_movie_details(movie_cd):
    try:
        url = settings.API_URL + '?key=' + settings.API_KEY + '&movieCd=' + \
            movie_cd
                    
        response = requests.get(url=url).json()
                
        movie_info = response['movieInfoResult']['movieInfo']
        
        nations = [ nation['nationNm'] for nation in movie_info['nations'] ]
        genres = [ genre['genreNm'] for genre in movie_info['genres'] ]
        directors = [ director['peopleNm'] for director in movie_info['directors'] ]
        actors = [ actor['peopleNm'] for actor in movie_info['actors'] ]
        
        movie = {
            'nation': nations,
            'genres': genres,
            'director': directors,
            'actors': actors
        }
    
        return movie

    except Exception as error:
        print(error)
