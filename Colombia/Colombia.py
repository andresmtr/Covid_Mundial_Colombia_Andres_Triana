#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 13:19:48 2020

@author: andresmauriciotrianareina
"""

import numpy as np
import pandas as pd
import chart_studio.plotly as py
import chart_studio.tools as tls

from chart_studio.grid_objs import Column, Grid

from IPython.display import IFrame
import plotly.graph_objs as go
import plotly.graph_objects as go
import cufflinks as cf
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import show
from pandas.plotting import register_matplotlib_converters
#%matplotlib inline
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly
import plotly.express as px
import time
from datetime import date, timedelta
from datetime import time
from datetime import datetime


import json
from urllib.request import urlopen
with urlopen('https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/be6a6e239cd5b5b803c6e7c2ec405b793a9064dd/Colombia.geo.json') as response:
    counties = json.load(response)


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


##############################
#Clean data



import requests

url = 'https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD&bom=true&format=true'

myfile = requests.get(url)

### Descagar la base de datos y guardar los datos, esta ruta se debe cambiar en donde alojan los datos

open('/Users/andresmauriciotrianareina/Documents/Cursos_desarrollo/Data_science/My_excercise/0_prueba/Casos_positivos_de_COVID-19_en_Colombia.csv', 'wb').write(myfile.content)


### Buscar los datos donde se descargo la información

df = pd.read_csv('/Users/andresmauriciotrianareina/Documents/Cursos_desarrollo/Data_science/My_excercise/0_prueba/Casos_positivos_de_COVID-19_en_Colombia.csv')

df ['Fecha identificación'] = df['fecha reporte web'].apply(lambda t: t.split('T')[0])

df['Numero'] = 1

df['Lugar'] = df['Departamento o Distrito ']


### Raplace bad values


df['Sexo'].replace(
    to_replace=['f'],
    value='F',
    inplace=True
)

df['Sexo'].replace(
    to_replace=['m'],
    value='M',
    inplace=True
)

df['atención'].replace(
    to_replace=['CASA'],
    value='Casa',
    inplace=True
)


df['Estado'].replace(
    to_replace=['LEVE'],
    value='Leve',
    inplace=True
)

df['Estado'].replace(
    to_replace=['NULL'],
    value='No indica la base de datos',
    inplace=True
)

df['atención'].replace(
    to_replace=['NULL'],
    value='No indica la base de datos',
    inplace=True
)

df['Estado'].replace(
    to_replace=['N/A'],
    value='No indica la base de datos',
    inplace=True
)

df['atención'].replace(
    to_replace=['HOSPITAL UCI'],
    value='Hospital UCI',
    inplace=True
)


df['atención'].replace(
    to_replace=['N/A'],
    value='No indica la base de datos',
    inplace=True
)


df['atención'].replace(
    to_replace=['hospital'],
    value='Hospital',
    inplace=True
)


##### reemplazar departamentos


df['Lugar'].replace(
    to_replace=['Bogotá D.C.'],
    value='SANTAFE DE BOGOTA D.C',
    inplace=True
)


df['Lugar'].replace(
    to_replace=['Barranquilla D.E.'],
    value='ATLANTICO',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Atlántico'],
    value='ATLANTICO',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Valle del Cauca'],
    value='VALLE DEL CAUCA',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Cartagena D.T. y C.'],
    value='BOLIVAR',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Antioquia'],
    value='ANTIOQUIA',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Nariño'],
    value='NARIÑO',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Cundinamarca'],
    value='CUNDINAMARCA',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Amazonas'],
    value='AMAZONAS',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Sucre'],
    value='SUCRE',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Chocó'],
    value='CHOCO',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Buenaventura D.E.'],
    value='VALLE DEL CAUCA',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Meta'],
    value='META',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Cesar'],
    value='CESAR',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Santa Marta D.T. y C.'],
    value='MAGDALENA',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Córdoba'],
    value='CORDOBA',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Bolívar'],
    value='BOLIVAR',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Tolima'],
    value='TOLIMA',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Santander'],
    value='SANTANDER',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Magdalena'],
    value='MAGDALENA',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['La Guajira'],
    value='LA GUAJIRA',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Risaralda'],
    value='RISARALDA',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Cauca'],
    value='CAUCA',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Boyacá'],
    value='BOYACA',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Norte de Santander'],
    value='NORTE DE SANTANDER',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Huila'],
    value='HUILA',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Caldas'],
    value='CALDAS',
    inplace=True
)


df['Lugar'].replace(
    to_replace=['Quindío'],
    value='QUINDIO',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Arauca'],
    value='ARAUCA',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Casanare'],
    value='CASANARE',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Caquetá'],
    value='CAQUETA',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Guaviare'],
    value='GUAVIARE',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Putumayo'],
    value='PUTUMAYO',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Vaupés'],
    value='VAUPES',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Archipiélago de San Andrés Providencia y Santa Catalina'],
    value='ARCHIPIELAGO DE SAN ANDRES PROVIDENCIA Y SANTA CATALINA',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Guainía'],
    value='GUAINIA',
    inplace=True
)

df['Lugar'].replace(
    to_replace=['Vichada'],
    value='VICHADA',
    inplace=True
)


#### Differents values


#Sexo = pd.DataFrame(df['Sexo'].value_counts())
#print (Sexo)

#Sexo
Sexo = df.pivot_table(index='Sexo', values='Numero',aggfunc='count').reset_index()
#Atención contagiados
Atención = df.pivot_table(index='atención', values='Numero',aggfunc='count').reset_index()
#Edad contagiados
Edad = df.pivot_table(index='Edad', values='Numero',aggfunc='count').reset_index()
#Suma casos
suma_casos_zona = df.groupby( ['Lugar'] ).sum().reset_index()
#Fecha
Fecha = df.groupby(['Fecha identificación']).count().reset_index()
#Fecha sexo
Fecha_sexo = df.groupby(['Fecha identificación', 'Sexo']).count().reset_index()





#Sexo fallecidos

SF = df['atención'] == 'Fallecido'
Solo_Fallecidos = df[SF]


Solo_Fallecidos ['Fecha de muerte f'] = Solo_Fallecidos['Fecha de muerte'].apply(lambda t: t.split('T')[0])

Suma_Solo_Fallecidos = Solo_Fallecidos.groupby( ['Lugar'] ).sum().reset_index()


Fallecidos_Fecha = Solo_Fallecidos.groupby( ['Fecha de muerte f'] ).sum().reset_index()


Fallecidos_Fecha_sexo = Solo_Fallecidos.groupby( ['Fecha de muerte f', 'Sexo'] ).sum().reset_index()



#print (Solo_Fallecidos.head())


Sexo_fallecidos = Solo_Fallecidos.pivot_table(index='Sexo', values='Numero',aggfunc='count').reset_index()

Edad_fallecidos = Solo_Fallecidos.pivot_table(index='Edad', values='Numero',aggfunc='count').reset_index()




#otros


Cont = df['Numero'].count()
#print (Contagiados)

Solo_fall_count = Solo_Fallecidos.groupby( ['Edad','Sexo'] ).sum().reset_index()



muer1 = df['atención'] == 'Fallecido'
muer2 = df[muer1]

Fall = muer2['Numero'].count()
#print (Fallecidos)



def figures_to_html(figs, filename="Contagios_sexo.html"):
    Colombia_Covid = open(filename, 'w')
    Colombia_Covid.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        Colombia_Covid.write(inner_html)
    Colombia_Covid.write("</body></html>" + "\n")
    
     
    
fig1 = px.bar(Sexo, 
              x = 'Sexo', 
              y = 'Numero',
              labels = {'x':'sexo','y':'Número personas contagiadas'}) 


figures_to_html([fig1])



def figures_to_html(figs, filename="Atención_contagiados.html"):
    Colombia_Covid = open(filename, 'w')
    Colombia_Covid.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        Colombia_Covid.write(inner_html)
    Colombia_Covid.write("</body></html>" + "\n")
    
     
    
fig1 = px.bar(Atención, 
              x = 'atención', 
              y = 'Numero',
              labels = {'x':'Atención','y':'Número de personas por atención'}) 


figures_to_html([fig1])


def figures_to_html(figs, filename="Contagios_Edad.html"):
    Colombia_Covid = open(filename, 'w')
    Colombia_Covid.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        Colombia_Covid.write(inner_html)
    Colombia_Covid.write("</body></html>" + "\n")
    
     
    
fig1 = px.histogram(df, 
              x = 'Edad')


figures_to_html([fig1])



def figures_to_html(figs, filename="Fallecidos_Sexo.html"):
    Colombia_Covid = open(filename, 'w')
    Colombia_Covid.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        Colombia_Covid.write(inner_html)
    Colombia_Covid.write("</body></html>" + "\n")
    
     
    
fig1 = px.bar(Sexo_fallecidos, 
              x = 'Sexo', 
              y = 'Numero',
              labels = {'x':'Sexo','y':'Número de fallecidos'})


figures_to_html([fig1])



def figures_to_html(figs, filename="Fallecidos_edad.html"):
    Colombia_Covid = open(filename, 'w')
    Colombia_Covid.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        Colombia_Covid.write(inner_html)
    Colombia_Covid.write("</body></html>" + "\n")
    
     
    
fig1 = px.histogram(Solo_Fallecidos, 
              x = 'Edad')


figures_to_html([fig1])



def figures_to_html(figs, filename="Mapa_Contagiados.html"):
    Colombia_Covid = open(filename, 'w')
    Colombia_Covid.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        Colombia_Covid.write(inner_html)
    Colombia_Covid.write("</body></html>" + "\n")
    
     
    
locs = suma_casos_zona['Lugar']

for loc in counties['features']:
    loc['id'] = loc['properties']['NOMBRE_DPT']
fig1 = go.Figure(go.Choroplethmapbox(
                    geojson=counties,
                    locations=locs,
                    z=suma_casos_zona['Numero'],
                    colorscale='Viridis',
                    colorbar_title="Contagiados"))
fig1.update_layout(mapbox_style="carto-positron",
                        mapbox_zoom=3.4,
                        mapbox_center = {"lat": 4.570868, "lon": -74.2973328})


figures_to_html([fig1])


def figures_to_html(figs, filename="Mapa_muertes.html"):
    Colombia_Covid = open(filename, 'w')
    Colombia_Covid.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        Colombia_Covid.write(inner_html)
    Colombia_Covid.write("</body></html>" + "\n")
    
     
    
locs2 = Suma_Solo_Fallecidos['Lugar']


for loc in counties['features']:
    loc['id'] = loc['properties']['NOMBRE_DPT']
fig1 = go.Figure(go.Choroplethmapbox(
                    geojson=counties,
                    locations=locs2,
                    z=Suma_Solo_Fallecidos['Numero'],
                    colorscale='Viridis',
                    colorbar_title="Muertes"))
fig1.update_layout(mapbox_style="carto-positron",
                        mapbox_zoom=3.4,
                        mapbox_center = {"lat": 4.570868, "lon": -74.2973328})


figures_to_html([fig1])

def figures_to_html(figs, filename="Fecha_Contagio.html"):
    Colombia_Covid = open(filename, 'w')
    Colombia_Covid.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        Colombia_Covid.write(inner_html)
    Colombia_Covid.write("</body></html>" + "\n")
    
     
    
fig1 = px.line(Fecha, 
              x = 'Fecha identificación', 
              y = 'Numero',
              labels = {'x':'Fecha de contagio','y':'Número de contagios'})


figures_to_html([fig1])


def figures_to_html(figs, filename="Fecha_Contagio_sexo.html"):
    Colombia_Covid = open(filename, 'w')
    Colombia_Covid.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        Colombia_Covid.write(inner_html)
    Colombia_Covid.write("</body></html>" + "\n")
    
     
    
fig1 = px.line(Fecha_sexo, 
              x = 'Fecha identificación', 
              y = 'Numero',
              color='Sexo',
              labels = {'x':'Fecha de contagio','y':'Número de contagios por sexo'})


figures_to_html([fig1])





def figures_to_html(figs, filename="Tabla_contagiados_fallecidos.html"):
    Colombia_Covid = open(filename, 'w')
    Colombia_Covid.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        Colombia_Covid.write(inner_html)
    Colombia_Covid.write("</body></html>" + "\n")


total = df['Numero'].count()

muer1 = df['atención'] == 'Fallecido'
muer2 = df[muer1]

muer3 = muer2['Numero'].count()


Rec1 = df['atención'] == 'Recuperado'
Rec2 = df[Rec1]

Rec3 = Rec2['Numero'].count()


Today = date.today()-timedelta(days=1)
fecha2 = Today.strftime("%Y-%m-%d")

total_Fall = pd.DataFrame({'Contagiados': [total],'Fallecidos': [muer3], 'Recuperados':[Rec3], 'Fecha': [fecha2]})
                            
total_Fall  


fig1 = go.Figure(data=[go.Table(
    header=dict(values=list(total_Fall.columns),
                fill_color='rgba(15, 78, 64, 0.1)',
                align='center'),
    cells=dict(values=[total_Fall.Contagiados, total_Fall.Fallecidos, total_Fall.Recuperados,total_Fall.Fecha ],
               fill_color='rgba(255, 255, 255, 0.1)',
               align='center',
               format = [",.0f", ",.0f",",.0f",None]))
])

figures_to_html([fig1])


def figures_to_html(figs, filename="Fallecidos_sexo_edad.html"):
    Colombia_Covid = open(filename, 'w')
    Colombia_Covid.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        Colombia_Covid.write(inner_html)
    Colombia_Covid.write("</body></html>" + "\n")
    
     
    
fig1 = px.scatter(Solo_fall_count, 
              x = 'Edad', 
              y = 'Numero',    
              color = 'Sexo',
              labels = {'x':'Edad','y':'Número de muertes por edad'})


figures_to_html([fig1])


fig = px.choropleth_mapbox(suma_casos_zona, geojson=counties, color="Numero",
                           locations="Lugar", featureidkey="properties.NOMBRE_DPT",
                           center={"lat": 4.570868, "lon": -74.2973328},
                           mapbox_style="carto-positron", zoom=3.4)

fig.show()



