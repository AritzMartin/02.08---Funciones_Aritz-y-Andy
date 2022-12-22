import urllib.request

def lector_link(link):
    file = urllib.request.urlopen(link)
    contenido = file.read()
    print(len(contenido.split()))
    return

link = 'https://www.marca.com/'

lector_link(link)

