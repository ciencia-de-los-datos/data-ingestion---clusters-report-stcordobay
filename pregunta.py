"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():
    dat=pd.read_fwf('./clusters_report.txt', skiprows=4, 
                names=['cluster', 'cantidad_de_palabras_clave', 
                       'porcentaje_de_palabras_clave', 'principales_palabras_clave'])

    dat.loc[:,'principales_palabras_clave']=dat.fillna(method='ffill').groupby('cluster')['principales_palabras_clave'].transform(lambda x: ' '.join(x))
    
    dat=dat.dropna().reset_index()
    dat.loc[:,'principales_palabras_clave']=dat.principales_palabras_clave.str.replace(r'\s+', ' ', 
                                                                                   regex=True).str.replace('.','')
    dat=dat.drop(columns='index')
    
    dat['porcentaje_de_palabras_clave']=dat['porcentaje_de_palabras_clave'].str[:-2].str.replace(',','.').astype(float)
    #
    # Inserte su código aquí
    #

    return dat
