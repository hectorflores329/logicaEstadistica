import pandas as pd

df = pd.read_excel('estadísticas-regionales-nuevo.xlsx', sheet_name='Links')

def principal():
    print("INFO: Comenzando descarga.")
    descarga()
    print("INFO: Descarga finalizada.")

def descarga():

    # try:

    for i, index in df.iterrows():
        
        tema = df['Tema'][i]
        nombre = df['Nombre'][i]
        region = df['Región'][i]
        url = df['Link'][i]
            
        #ext = pathlib.Path(url)
        #extType = ext.suffix.split("?")
        
        dfData = pd.read_excel(url)
        dfData.to_excel('files/' + str(tema) + ' - ' + str(nombre) + ' - ' + str(region) + str(".xlsx"), index=False)
    # except:
        # print("INFO: Error al descargar los archivos.")


if __name__ == '__main__':
    principal()