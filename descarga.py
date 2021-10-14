import pandas as pd
import requests
import pathlib
import os
import time
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

        page = ''
        while page == '':
            try:
                page = requests.get(url)
                break
            except:
                print("Connection refused by the server..")
                print("Let me sleep for 5 seconds")
                print("ZZzzzz...")
                time.sleep(5)
                print("Was a nice sleep, now let me continue...")
                continue

        # downloadFile = requests.get(url)
        open('files/' + str(tema) + ' - ' + str(nombre) + ' - ' + str(region) + str(extType[0]), 'wb').write(page.content)


if __name__ == '__main__':
    principal()
