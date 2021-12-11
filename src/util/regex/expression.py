import re


def get_movie_cd(text):
    lis = re.findall('[0-9]', text)
    movie_cd = ''.join(lis)
    return movie_cd