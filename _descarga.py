import pandas as pd
import pathlib
import requests

df = pd.read_excel('estadísticas-regionales-nuevo.xlsx', sheet_name='Links')

def descarga():
    
    print("Descargando...")
    try:
        for i, index in df.iterrows():
            
            tema = df['Tema'][i]
            nombre = df['Nombre'][i]
            region = df['Región'][i]
            url = df['Link'][i]

            ext = pathlib.Path(url)
            extType = ext.suffix.split("?")

            _file = requests.get(url)
            open('files/' + str(tema) + ' - ' + str(nombre) + ' - ' + str(region) + str(extType[0]), 'wb').write(_file.content)

        print("•• Archivos descargados correctamente.")

    except:
        print("-- Error al descargar los archivos.")
