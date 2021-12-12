from src.util import get_movie_details, get_movie_information

def lambda_handler(event, context):
    movies = get_movie_information(OPTION='PRODUCTION')
    
    for movie in movies:
        movie_info = get_movie_details(movie['movie_cd'])
        movie.update(movie_info)
    
    return


if __name__ == '__main__':
    movies = get_movie_information()
    
    for movie in movies:
        movie_info = get_movie_details(movie['movie_cd'])
        movie.update(movie_info)
    