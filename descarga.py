import pandas as pd
import requests
import pathlib
import os
import time
import urllib


requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':RC4-SHA'
try:
    requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += ':RC4-SHA'
except AttributeError:
    # no pyopenssl support used / needed / available
    pass

df = pd.read_excel('estadísticas-regionales-nuevo.xlsx', sheet_name='Links')

def principal():
    descarga()

def descarga():
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':RC4-SHA'
    
    for i, index in df.iterrows():
    
        tema = df['Tema'][i]
        nombre = df['Nombre'][i]
        region = df['Región'][i]
        url = df['Link'][i]
            
        ext = pathlib.Path(url)
        extType = ext.suffix.split("?")


        downloadFile = requests.get(url, verify=False)
        open('files/' + str(tema) + ' - ' + str(nombre) + ' - ' + str(region) + str(extType[0]), 'wb').write(downloadFile.content)


if __name__ == '__main__':
    principal()
