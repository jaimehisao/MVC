import requests

root_url = "https://rickandmortyapi.com/api"

session = requests.Session()


def get_all_characters():
    characters = []
    url = f"{root_url}/character"
    curr_page = 2
    first_page = session.get(url).json()
    num_pages = first_page['info']['pages']

    response = requests.get(url)
    print(response.json())

    for character in response.json()["results"]:
        characters.append(character["name"])
        print(character["name"])

    while curr_page <= num_pages:
        response = session.get(url, params={"page": curr_page})
        for character in response.json()["results"]:
            characters.append(character["name"])
            print(character["name"])
        curr_page += 1
    return characters


def get_all_locations():
    locations = []
    url = f"{root_url}/location"
    curr_page = 2
    first_page = session.get(url).json()
    num_pages = first_page['info']['pages']

    response = requests.get(url)
    print(response.json())

    for location in response.json()["results"]:
        locations.append(location["name"])
        print(location["name"])

    while curr_page <= num_pages:
        response = session.get(url, params={"page": curr_page})
        for location in response.json()["results"]:
            locations.append(location["name"])
            print(location["name"])
        curr_page += 1
    return locations


def get_all_episodes():
    episodes = []
    url = f"{root_url}/episode"
    curr_page = 2
    first_page = session.get(url).json()
    num_pages = first_page['info']['pages']

    response = requests.get(url)
    print(response.json())

    for episode in response.json()["results"]:
        episodes.append(episode["name"])
        print(episode["name"])

    while curr_page <= num_pages:
        response = session.get(url, params={"page": curr_page})
        for episode in response.json()["results"]:
            episodes.append(episode["name"])
            print(episode["name"])
        curr_page += 1
    return episodes


chars = get_all_characters()
locs = get_all_locations()
epis = get_all_episodes()
print(len(chars))
