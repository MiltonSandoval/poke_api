
import os
import requests
import certifi
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

def menu():
    print("Bienvenido al menu de la pokeAPI \n")
    print("1. Buscar pokemon \n"
          "2. Buscar pokemones locales \n"
          "3. Agregar un Pokemon de manera local \n"
          "4. Salir \n")
    opcion = input("Ingrese su opcion:")
    return opcion

def EsperarTecla(num):
    if num == 1:
        esperar = input("Ingrese cualquier tecla para salir :D \n")
        return 1
    elif num == 2:
        esperar = input("Ingresa una opcion Valida!!! \n")
        return 1
    esperar = input("Lo siento a ocurrido un error inesperado,"
                    "ingrese cualquier tecla para volver al menu principal \n")
    return 0

while True:
    opcion = menu()
    if opcion == "1":
        url = 'http://pokeapi.co/api/v2/pokemon/1/'  # Cambia el número para obtener otro Pokémon
        req = requests.get(url)
        pokemon_data = req.json()
        print(f"Nombre del Pokémon: {pokemon_data['name']}")
        print(f"Habilidades: {', '.join(ability['ability']['name'] for ability in pokemon_data['abilities'])}")
    elif opcion == "2":
        pass
    elif opcion == "3":
        pass
    elif opcion == "4":
        EsperarTecla(1)
        break
    else:
        EsperarTecla(2)
