import requests
import urllib3
"""
url = 'http://pokeapi.co/api/v2/pokemon/1/'  # Cambia el número para obtener otro Pokémon
req = requests.get(url)
pokemon_data = req.json()
print(f"Nombre del Pokémon: {pokemon_data['name']}")
print(f"Habilidades: {', '.join(ability['ability']['name'] for ability in pokemon_data['abilities'])}")
"""
urllib3.disable_warnings()

class Pokemon:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def buscar(self):
        try:
            url = f"http://pokeapi.co/api/v2/pokemon/{self.nombre}/"
            req = requests.get(url, verify=False)
            Pokedex = req.json()
            print("-" * 15)
            print(f"Nombre: {Pokedex['name']} \n"
                f"Numero en la Pokedex: {Pokedex['id']} \n"
                f"Tipo: {Pokedex['types'][0]['type']['name']}")
            print("-"*15)
        except:
            print("Asegurate de ingresar bien el nombre del pokemon :D")

def Tipo(tipos:list):
    for elementos in tipos:
        for type in elementos:
            tipo += type['name']
    return tipo


#pikachu = Pokemon("pikachu")

#pikachu.buscar()

