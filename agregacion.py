import pandas as pd
import time
import requests

def principal():
    agregacion()

def years(year):
    
    year = str(year) + "  00:00:00"
    return year

def months(mes):
    
    mes = mes.lower().replace(" ", "")
    
    meses = {
        'enero': '01/01/',
        'febrero': '01/02/',
        'marzo': '01/03/',
        'abril': '01/04/',
        'mayo': '01/05/',
        'junio': '01/06/',
        'julio': '01/07/',
        'agosto': '01/08/',
        'septiembre': '01/09/',
        'octubre': '01/10/',
        'noviembre': '01/11/',
        'diciembre': '01/12/'
    }
    
    return meses[mes]

def agregacion():
    dfRegion = pd.read_excel("regiones.xlsx")

    dfTabla = dfData.loc[:, colsExsistentes]
    dfTabla.columns = cols

    dfTabla["Glosa Variable"] = dfTabla["Glosa Variable"].apply(lambda x : years(x))
    dfTabla["Mes"] = dfTabla["Mes"].apply(lambda x : months(x))
    dfTabla["Glosa Variable"] = dfTabla["Mes"] + dfTabla["Glosa Variable"]

    del dfTabla["Mes"]
    dfTabla["Glosa Variable"] = pd.to_datetime(dfTabla["Glosa Variable"], format="%d/%m/%Y  %H:%M:%S")



    dfT = dfTabla.transpose()
    dfT.columns = dfT.iloc[0]
    dfT = dfT.reset_index()

    dfT = dfT.drop(range(1))
    dfT.rename(columns={'index': 'Glosa Variable',
                        'Glosa Variable': 'index'}, inplace=True)

    dfCero = pd.DataFrame()

    for k in cols[2:]:
        
        dfVariable = dfDescriptor[dfDescriptor["Glosa Variable"] == str(k)]

        dfVariable["Código región"] = cRegion
        dfVariable["Glosa región"] = region
        dfVariable["Periodicidad"] = periodicidad

        del dfVariable["Fuente"]

        dfVariable
        
        dfv2 = dfT[dfT["Glosa Variable"] == str(k)]
        
        merged = pd.merge(left=dfVariable,right=dfv2, how='left', left_on='Glosa Variable', right_on='Glosa Variable')
        dfCero = pd.concat([dfCero, merged], axis=0)

    dfER = pd.read_excel("estadísticas-regionales.xlsx")
    _df = pd.concat([dfER, dfCero])
    _df.to_excel("estadísticas-regionales.xlsx", index=False)

if __name__ == '__main__':
    principal()