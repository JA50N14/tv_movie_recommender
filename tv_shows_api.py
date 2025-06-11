import requests
import json
from config import ACCESS_TOKEN


def show_search_title(show_title):
    url = "https://api.themoviedb.org/3/search/tv"
    payload = {"query": show_title, "include_adult": "false", "language": "en-US", "page": "1"}
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    response = requests.get(url, params=payload, headers=headers)
    python_obj = json.loads(response.text)
    show_list = [(show['name'], show['id'], f"{show['overview'][:85]}...") for show in python_obj['results']]
    return show_list 


def show_recommender(title_and_id):
    url = f"https://api.themoviedb.org/3/tv/{title_and_id[1]}/recommendations"
    payload = {"language": "en-US", "page": "1"}
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    response = requests.get(url, params=payload, headers=headers)
    python_obj = json.loads(response.text)
    show_list = [(show['name'], show['first_air_date'], show['vote_average'], show['overview']) for show in python_obj['results']]
    print('--------------------------------------------------------------------------------------------------------------')
    if len(show_list) == 0:
        print(f"There are no recommendations based on \"{title_and_id[0]}\".")
    for show in show_list:
        print(f"-Show Title: {show[0]}\n-First Air Date: {show[1]}\n-Vote Average: {show[2]}\n-Overview: {show[3]}")
        print('----------------------------------------------------------------------------------------------------------')
    return

def show_similar(title_and_id):
    url = f"https://api.themoviedb.org/3/tv/{title_and_id[1]}/similar"
    payload = {"language": "en-US", "page": "1"}
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    response = requests.get(url, params=payload, headers=headers)
    python_obj = json.loads(response.text)
    show_list = [(show['name'], show['first_air_date'], show['vote_average'], show['overview']) for show in python_obj['results']]
    print('--------------------------------------------------------------------------------------------------------------')
    if len(show_list) == 0:
        print(f"There are no similar shows based on \"{title_and_id[0]}\".")
    for show in show_list:
        print(f"-Show Title: {show[0]}\n-First Air Date: {show[1]}\n-Vote Average: {show[2]}\n-Overview: {show[3]}")
        print('----------------------------------------------------------------------------------------------------------')
    return

def show_description(title_and_id):
    url = f"https://api.themoviedb.org/3/tv/{title_and_id[1]}"
    payload = {"language": "en-US", "page": "1"}
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    response = requests.get(url, params=payload, headers=headers)
    python_obj = json.loads(response.text)
    show_data = {'created_by': [], 'first_air_date': python_obj['first_air_date'], 'genres': [], 'last_air_date': python_obj['last_air_date'], 'name': python_obj['name'], 'next_episode_to_air': python_obj['next_episode_to_air'], 'number_of_seasons': python_obj['number_of_seasons'], 'overview': python_obj['overview'], 'status': python_obj['status'], 'vote_average': python_obj['vote_average']}
    for creator in python_obj['created_by']:
        show_data['created_by'].append(creator["name"])
    
    for genre in python_obj['genres']:
        show_data['genres'].append(genre["name"])

    labels = {'name': 'Show Name', 'genres': 'Genres', 'vote_average': 'Vote Average', 'first_air_date': 'First Air Date', 'last_air_date': 'Last Air Date', 'next_episode_to_air': 'Next Episode to Air', 'status': 'Status', 'number_of_seasons': 'Number of Seasons', 'created_by': 'Created By', 'overview': 'Overview'}

    print('--------------------------------------------------------------------------------------------------------------')
    for key in labels:
        value = show_data[key]
        if isinstance(value, list):
            value = ', '.join(value)
        print(f"-{labels[key]}: {value}")
    print('--------------------------------------------------------------------------------------------------------------')
    return

