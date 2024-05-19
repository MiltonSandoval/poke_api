
import os
from openpyxl import Workbook
from Modulos.class_pokemon import *

wb = Workbook()
ws = wb.active

def menu():
    print("\n Bienvenido al menu de la pokeAPI \n")
    print("1. Buscar pokemon \n"
          "2. Pokemones locales \n"
          "3. Salir \n")
    opcion = input("Ingrese su opcion:")
    return opcion


def EsperarTecla(num):
    if num == 1:
        esperar = input("Ingrese cualquier tecla :D \n")
        return 1
    elif num == 2:
        esperar = input("Ingresa una opcion Valida!!! \n")
        return 1
    esperar = input("Lo siento a ocurrido un error inesperado,"
                    "ingrese cualquier tecla para volver al menu principal \n")
    return 0

def buscar_pokemon():
        nombre = input("Ingresa el nombre del pokemon o su numero en la pokedex:")
        poke = Pokemon(nombre.lower())
        poke.buscar()

while True:
    opcion = menu()
    if opcion == "1":
        buscar_pokemon()
        EsperarTecla(1)
    elif opcion == "2":
        pass
    elif opcion == "3":
        EsperarTecla(1)
        break
    else:
        EsperarTecla(2)
