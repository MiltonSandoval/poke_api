import requests
import urllib3

#Esta funcion evita que se espanee el mensaje del ssl al hacer una consulta con el verify desactivado
urllib3.disable_warnings()

#Clase que recibe de parametro el nombre del pokemon y que tiene un metodo para buscar al pokemon en la api
class Pokemon:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def buscar(self):
        try:
            url = f"http://pokeapi.co/api/v2/pokemon/{self.nombre}/"
            req = requests.get(url, verify=False)
            Pokedex = req.json()
            print("-" * 20)
            print(f"Nombre: {Pokedex['name']} \n"
                f"Numero en la Pokedex: {Pokedex['id']} \n"
                f"Tipo: {Tipo(Pokedex['types'])}")
            print("-" * 20)
        except:
            print("Lo siento acaba de ocurrir un error inesperado, asegurate de escribir bien el nombre o el numero del pokemon o intenta mas tarde")

#Funcion que sirve para imprimir los tipos de los pokemones, en caso de que tenga mas de 1
def Tipo(tipos):
    tipo = []
    for elementos in tipos:
            tipo.append(elementos['type']['name'])
    tipo = ", ".join(tipo)
    return tipo
