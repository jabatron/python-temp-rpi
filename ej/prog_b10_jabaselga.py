""" 
Detalles:

Extraccion de datos de cuentas de instagram

Requerimientos:

Crea un programa que a partir de un nombre de usuario de instagram ingresada por el usuario determine si la cuenta existe.

Si existe debe mostrar los siguientes datos de forma ordenada:

°Nombre de usuario
°Nombre
°Cantidad de seguidores
°Cantidad de seguidos
°Cantidad de publicaciones
°Si la cuenta es privada o publica


Programas completados:

code: progb_10_tuuser.py
@aprenderpython
#webscraping

LIBRERIAS ADICIONALES

pip install gazpacho
pip install selenium
chrome & chromedriver to use selenium

"""

from gazpacho import get, Soup

# para usar selenium
try:
    from selenium.webdriver import Chrome
    from selenium.webdriver.chrome.options import Options
    sl=True
except:
    print ('Sin selenium va a ser dificil sacar el tipo de cuenta ...')
    sl=False


url='https://www.instagram.com/'

def pedir_usuario():
    usuario=input('Introduzca un usuario para comprobar: ')
    return usuario

def paser_selenium (page):
    chrome_options=Options()
    chrome_options.add_argument("--headless")
    try:
        browser=Chrome(options=chrome_options)
    except:
        return 'Me fatltan componetes de chrome para sacar el tipo de cuenta.'
    
    browser.get(page)
    browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()

    try:
        tipo=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div/div/h2')
        tipo=tipo.text
    except:
        tipo='La cuenta es pública'
    
    return tipo

def comprobar_estado(usuario, sl):
    url_user=url+usuario+'/?hl=es'
    try:
        html=get(url_user)
    except:
        return None

    html_s=Soup(html)
    a=html_s.find('meta', attrs={'property':'og:description'})
    dic=a.attrs
    n=dic['content'].replace('-',',')
    n=n.split(',')
    data=(x.strip() for x in n)
    # ('431 Followers', '872 Following', '294 Posts', 'See Instagram photos and videos from JP (@juanpedro)')

    seguidores, seguidos, publicaciones, usuario = data
    *_, usuario = usuario.split(' ')
    # '@juanpedro'
    usuario = usuario[1:-1]

    if sl:
        tipo=paser_selenium(url_user)
    else:
        tipo='No tienes selenium instaldo, imposible sacar el tipo cuenta...'


    return usuario, seguidores, seguidos, publicaciones, tipo

def imprimir_datos(usuario, seguidores, seguidos, publicaciones, tipo):
    print (f'{usuario}'.center(40,"*"))
    print (seguidores)
    print (seguidos)
    print (publicaciones)
    print (tipo)

if __name__ == "__main__":
    
    user=pedir_usuario()
    try:
        usuario, seguidores, seguidos, publicaciones, tipo = comprobar_estado(user, sl)
        imprimir_datos(usuario, seguidores, seguidos, publicaciones, tipo)
    except TypeError:
        print ("El usuario no existe..")
    
    print ("Fin del juego".center(40, "*"))