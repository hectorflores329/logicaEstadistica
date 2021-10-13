import pandas as pd
import math

def principal():
    descarga1()

# LÓGICA / DESCARGA 1

filename = "files/Electricidad, Gas y Agua - Distribución Electrica - Biobio.xlsx"

def registros(Year, Mes, Total, Residencial, Comercial, Minera, Agricola, Industrial, Varios):
    
    diccionario = {}
    
    diccionario["Año"] = Year
    diccionario["Mes"] = Mes
    diccionario["Total"] = Total
    diccionario["Residencial"] = Residencial
    diccionario["Comercial"] = Comercial
    diccionario["Minería"] = Minera
    diccionario["Agrícola"] = Agricola
    diccionario["Industrial"] = Industrial
    diccionario["Varios"] = Varios
    
    return diccionario


def descarga1():

    df = pd.read_excel(filename, skiprows=4)

    del df["Unnamed: 9"]
    del df["Unnamed: 10"]

    df.columns = ["Año", "Mes", "Total", "Residencial", "Comercial", "Minería", "Agrícola", "Industrial", "Varios"]

    datos = []

    for i, j in df.iterrows():

        Year = df["Año"][i]
        Mes = df["Mes"][i]
        Total = df["Total"][i]
        Residencial = df["Residencial"][i]
        Comercial = df["Comercial"][i]
        Minera = df["Minería"][i]
        Agricola = df["Agrícola"][i]
        Industrial = df["Industrial"][i]
        Varios = df["Varios"][i]

        if(len(str(Year)) <= 7):

            _year = str(Year)[:4]

            x=float(_year)

            if(math.isnan(x)):
                pass
            else:
                if(int(_year) >= 2014):
                    diccionario = registros(str(_year), Mes, Total, Residencial, Comercial, Minera, Agricola, Industrial, Varios)
                    datos.append(diccionario.copy())
                else:
                    pass

    data = pd.DataFrame(datos)
    data.replace("-","",inplace=True)
    data.fillna(" ", inplace = True)
    data.to_excel("cFiles/Electricidad, Gas y Agua-Distribución Electrica-Biobío.xlsx", index=False)

    
if __name__ == '__main__':
    principal()
    