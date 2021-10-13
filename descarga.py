import pandas as pd
import requests
import pathlib
import os
import urllib

df = pd.read_excel('estadísticas-regionales-nuevo.xlsx', sheet_name='Links')

def principal():
    descarga()

def descarga():

    for i, index in df.iterrows():
    
        tema = df['Tema'][i]
        nombre = df['Nombre'][i]
        region = df['Región'][i]
        url = df['Link'][i]
            
        ext = pathlib.Path(url)
        extType = ext.suffix.split("?")

        file = requests.get(url)
        open('files/' + str(tema) + ' - ' + str(nombre) + ' - ' + str(region) + str(extType[0]), 'wb').write(file.content)


if __name__ == '__main__':
    principal()