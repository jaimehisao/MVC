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


chars = get_all_characters()
print(len(chars))

