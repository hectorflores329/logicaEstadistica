import pandas as pd

df = pd.read_excel('estadísticas-regionales-nuevo.xlsx', sheet_name='Links')

def principal():
    descarga()

def descarga():

   for i, index in df.iterrows():
    
    tema = df['Tema'][i]
    nombre = df['Nombre'][i]
    region = df['Región'][i]
    url = df['Link'][i]
        
    #ext = pathlib.Path(url)
    #extType = ext.suffix.split("?")
    
    dfData = pd.read_excel(url)
    dfData.to_excel('files/' + str(tema) + ' - ' + str(nombre) + ' - ' + str(region) + str(".xlsx"), index=False)

    print("ARCHIVOS DESCARGADO CORRECTAMENTE")

if __name__ == '__main__':
    principal()