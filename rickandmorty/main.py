import requests
from dto.character import Character
from dto.location import Location
from dto.episode import Episode

root_url = "https://rickandmortyapi.com/api"

session = requests.Session()


def get_all_characters():
    characters = []
    url = f"{root_url}/character"
    curr_page = 2
    first_page = session.get(url).json()
    num_pages = first_page['info']['pages']

    response = requests.get(url)

    for character in response.json()["results"]:
        characters.append(Character(name=character["name"],
                                    species=character["species"],
                                    gender=character["gender"],
                                    number_of_episodes=0))

    while curr_page <= num_pages:
        response = session.get(url, params={"page": curr_page})
        for character in response.json()["results"]:
            characters.append(character["name"])
        curr_page += 1
    return characters


def get_all_locations():
    locations = []
    url = f"{root_url}/location"
    curr_page = 2
    first_page = session.get(url).json()
    num_pages = first_page['info']['pages']

    response = requests.get(url)

    for location in response.json()["results"]:
        locations.append(Location(name=location["name"],
                                  _type=location["type"],
                                  dimension=location["dimension"],
                                  number_of_residents=0))

    while curr_page <= num_pages:
        response = session.get(url, params={"page": curr_page})
        for location in response.json()["results"]:
            locations.append(location["name"])
        curr_page += 1
    return locations


def get_all_episodes():
    episodes = []
    url = f"{root_url}/episode"
    curr_page = 2
    first_page = session.get(url).json()
    num_pages = first_page['info']['pages']

    response = requests.get(url)

    for episode in response.json()["results"]:
        episodes.append(Episode(name=episode["name"],
                                air_date=episode["air_date"],
                                episode_number=episode["episode"],
                                number_of_characters=0))

    while curr_page <= num_pages:
        response = session.get(url, params={"page": curr_page})
        for episode in response.json()["results"]:
            episodes.append(episode["name"])
        curr_page += 1
    return episodes


chars = get_all_characters()
locs = get_all_locations()
epis = get_all_episodes()
