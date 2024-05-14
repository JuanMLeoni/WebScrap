import pandas as pd;
import requests;
from pathlib import PurePath;
from bs4 import BeautifulSoup;

def ValorDoral(precio):
    url = 'https://dolarhoy.com/'
    contenido = requests.get(url)
    if contenido.ok:
        sopa = BeautifulSoup(contenido.text, 'html.parser')
        body = sopa.find(id = 'main_body ')
        Ven = body.find(class_ = 'venta')
        val = Ven.find(class_ = 'val')
        for v in val:
            str(v)
            V = v[1:]
        precio = precio * int(V)
        return precio
