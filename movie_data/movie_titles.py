import random

movies = {
    'last of the mohicans': {"release_date": "1992-09-25"},
    'donnie darko': {"release_date": "2001-01-18"},
    'magnolia': {"release_date": "1999-12-08"},
    'what we do in the shadows': {"release_date": "2014-06-19"},
    'the fountain': {"release_date": "2006-09-06"},
    'paprika': {"release_date": "2006-10-01"},
    'fight club': {"release_date": "1999-10-15"}
}


def random_movie():
    choice_tuple = random.choice(list(movies.items()))
    return {'title': choice_tuple[0], 'info': choice_tuple[1]}

