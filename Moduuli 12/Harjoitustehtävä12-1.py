"""

Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/. Käyttäjälle on näytettävä pelkkä vitsin teksti.

"""
import requests

def get_random_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    joke_data = response.json()
    return joke_data["value"]

def main():
    joke = get_random_joke()
    print(joke)

if __name__ == "__main__":
    main()