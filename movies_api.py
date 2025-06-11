import requests
import json
from config import ACCESS_TOKEN

def movie_search_title(movie_title):
    url = "https://api.themoviedb.org/3/search/movie"
    payload = {'query': movie_title, 'include_adult': 'false', 'language': 'en-US', 'page': '1'}
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    response = requests.get(url, params=payload, headers=headers)
    python_obj = json.loads(response.text)
    movie_list = [(movie["title"], movie["id"], f"{movie["overview"][:85]}...") for movie in python_obj["results"]]
    return movie_list


def movie_recommender(title_and_id):
    url = f"https://api.themoviedb.org/3/movie/{title_and_id[1]}/recommendations"
    payload = {'language': 'en-US', 'page': '1'}
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    response = requests.get(url, params=payload, headers=headers)
    python_obj = json.loads(response.text)
    movie_list = [(movie["title"], movie["release_date"], movie["vote_average"], movie["overview"]) for movie in python_obj["results"]]
    print('--------------------------------------------------------------------------------------------------------------')
    if len(movie_list) == 0:
        print(f"There are no recommendations based on \"{title_and_id[0]}\".")
    for movie in movie_list:
        print(f"-Movie Title: {movie[0]}\n-Release Date: {movie[1]}\n-Vote Average: {movie[2]}\n-Overview: {movie[3]}")
        print('----------------------------------------------------------------------------------------------------------')
    return


def movie_similar(title_and_id):
    url = f"https://api.themoviedb.org/3/movie/{title_and_id[1]}/similar"
    payload = {"language": "en-US", "page": "1"}
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    response = requests.get(url, params=payload, headers=headers)
    python_obj = json.loads(response.text)
    movie_list = [(movie["title"], movie["release_date"], movie["vote_average"], movie["overview"]) for movie in python_obj["results"]]
    print('--------------------------------------------------------------------------------------------------------------')
    if len(movie_list) == 0:
        print(f"There are no recommendations based on \"{title_and_id[0]}\".")
    for movie in movie_list:
        print(f"-Movie Title: {movie[0]}\n-Release Date: {movie[1]}\n-Vote Average: {movie[2]}\n-Overview: {movie[3]}")
        print('----------------------------------------------------------------------------------------------------------')
    return

def movie_description(title_and_id):
    url = f"https://api.themoviedb.org/3/movie/{title_and_id[1]}"
    payload = {"language": "en-US", "page": "1"}
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    response = requests.get(url, params=payload, headers=headers)
    python_obj = json.loads(response.text)
    
    movie_data = {'origin_country': [], 'overview': python_obj["overview"], 'genres': [], 'release_date': python_obj["release_date"], 'runtime': python_obj["runtime"], 'title': python_obj["title"], 'status': python_obj["status"], 'vote_average': python_obj['vote_average']}
    for country in python_obj['origin_country']:
        movie_data['origin_country'].append(country)
    
    for genre in python_obj['genres']:
        movie_data['genres'].append(genre["name"])

    labels = {'title': 'Movie Title', 'genres': 'Genres', 'origin_country': 'Origin Country', 'vote_average': 'Vote Average', 'release_date': 'Release Date', 'runtime': "Length (min)", 'status': 'Status', 'overview': 'Overview'}

    print('--------------------------------------------------------------------------------------------------------------')
    for key in labels:
        value = movie_data[key]
        if isinstance(value, list):
            value = ', '.join(value)
        print(f"-{labels[key]}: {value}")
    print('--------------------------------------------------------------------------------------------------------------')
    return



