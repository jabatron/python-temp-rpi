""" 
Detalles:

Determina si un pokemon existe

Requerimientos:

Crea un programa que verifique si existe un Pokémon, el usuario debe ingresar el nombre de algún Pokémon y luego usando webscraping verificaras si existe un Pokémon con ese nombre en una de las paginas proporcionadas u otras, si existe: Debe imprimirle en pantalla que existe el Pokémon, el nombre del Pokémon y el tipo de Pokémon que es, sino imprimir en pantalla 

Ej:Hemos encontrado tu Pokémon: 
   Nombre:Pikachu Tipo:Electrico
 Sino:
Tu Pokémon no ha sido encontrado o no existe

Webs donde pueden sacar informacion:
Link 1 (https://www.pokemon.com/es/pokedex/) 
Link 2 (https://pokemon.fandom.com/es/wiki/Lista_de_Pok%C3%A9mon) 

Nota: No es obligatorio solo limitarse a esas webs, pueden buscar otras, pero estas las pueden usar.


LIBRERIAS ADICIONALES

pip install beautifulsoup4
pip install lxml

"""
from requests import get
from bs4 import BeautifulSoup
import sys

def pedir_nombre ():
    nombre=input('Introduce el nombre de pokemon a verificar:')
    return nombre


def chequear_pokemon (pokemon):
    pokemon_com = 'https://www.pokemon.com/es/pokedex/' + pokemon
    tipo = []
    pokemonpage=get(pokemon_com)
    if pokemonpage.status_code != 200:
        return False, None
    else:
        soup=BeautifulSoup(pokemonpage.text, "lxml")
        for link in soup.find_all('a'):
            if 'type' in link.get('href'):
                tipo.append(link.text)
        tipo=set(tipo)
    return True, tipo

def chequear_fandom (pokemon):
    pokemonpage=get('https://pokemon.fandom.com/es/wiki/Lista_de_Pok%C3%A9mon')
    if pokemonpage.status_code == 200:
        tabla_pk = []
        pika = []
        pokemon=pokemon.title()
        dicc = {"title": pokemon}
        soup=BeautifulSoup(pokemonpage.text, 'lxml')
        tablas=soup.find_all('table', { "class" : "tabpokemon sortable mergetable"})
                    
        for t in tablas:
            if t.find_all('a', dicc):
                tabla_pk=t
        
        if not tabla_pk:
            return False, None
        
        tabla_pk.find_all('a', dicc)
        filas=tabla_pk.find_all('tr')
        for f in filas:
            if f.find_all('a', dicc):
                pika = f
        last=pika.find_all('a')
        la=[]
        for a in last:
            #print (a.attrs)
            if 'Tipo' in a.attrs['title']:
                la.append(a.attrs['title'])
        return True, la

# programa PRINCIPAL
if __name__ == "__main__":
    arguments_count=len(sys.argv)
    
    print ("________________________________________________________________________________")
    print ('Ejercicio b8. Determina si un determinado pokemon existe y de que tipo es.')
    print ('@jabaselga')
    print ("________________________________________________________________________________")

    if arguments_count > 2:
        print ('Para ejecutar el comando:')
        print (f'{sys.argv[0]} [pokemon_name]')

    elif arguments_count == 2:
        pokemon=sys.argv[1]
    else:   #hay que pedir el nombre del pokemon
        pokemon=pedir_nombre()

    es_pokemon, tipo = chequear_pokemon(pokemon)

    if es_pokemon:
        print (tipo)
    else:
        print ('Eso no es un pokemon')

    es_pokemon, tipo = chequear_fandom(pokemon)

    if es_pokemon:
        print (tipo)
    else:
        print ('Eso no es un pokemon')