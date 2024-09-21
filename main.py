
from Modulos.class_pokemon import *

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
    elif num == 3:
        esperar = input("Error de conexion")
        return 1
    esperar = input("Lo siento a ocurrido un error inesperado,"
                    "ingrese cualquier tecla para volver al menu principal \n")

def buscar_pokemon():
    try:
        nombre = input("Ingresa el nombre del pokemon o su numero en la pokedex:")
        poke = Pokemon(nombre.lower())
        diccionario_poke:dict = poke.Buscar()
        imprimir_poke(diccionario_poke['name'],diccionario_poke['id'],diccionario_poke['tipo'])
        EsperarTecla(1)
    except requests.ConnectionError:
        EsperarTecla(3)
    except:
        EsperarTecla(4)

def PokeLocal():
    try:
        nombre = input("Ingresa el nombre del pokemon o su numero en la pokedex:")
        poke =  Pokemon(nombre.lower())
        poke.BuscarLocal()
        EsperarTecla(1)
    except requests.ConnectionError:
        EsperarTecla(3)
        print("Lo sentimos no se logro agregar a la base local el pokemon que esta buscando \n")
    except ValueError:
        print("Error asegurate de escribir bien el nombre de tu pokemon")

while True:
    opcion = menu()
    if opcion == "1":
        buscar_pokemon()
    elif opcion == "2":
        PokeLocal()
    elif opcion == "3":
        EsperarTecla(1)
        break
    else:
        EsperarTecla(2)


