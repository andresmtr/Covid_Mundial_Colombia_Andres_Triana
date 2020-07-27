#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 13:19:48 2020

@author: andresmauriciotrianareina
"""

import numpy as np
import pandas as pd
import chart_studio.plotly as py
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
from datetime import date
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

today = date.today()
fecha = today.strftime("%Y-%m-%d")


### Data Name

df = pd.read_csv('Casos_positivos_de_COVID-19_en_Colombia.csv')

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
    to_replace=['N/A'],
    value='No indica la base de datos',
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
#print (Sexo)
#Atención contagiados
Atención = df.pivot_table(index='atención', values='Numero',aggfunc='count').reset_index()
#print (Atención)
#Edad contagiados
Edad = df.pivot_table(index='Edad', values='Numero',aggfunc='count').reset_index()
#print (Edad)

suma_casos_zona = df.groupby( ['Lugar'] ).sum().reset_index()





#Sexo fallecidos

SF = df['atención'] == 'Fallecido'
Solo_Fallecidos = df[SF]

Suma_Solo_Fallecidos = Solo_Fallecidos.groupby( ['Lugar'] ).sum().reset_index()

#print (Solo_Fallecidos.head())


Sexo_fallecidos = Solo_Fallecidos.pivot_table(index='Sexo', values='Numero',aggfunc='count').reset_index()

Edad_fallecidos = Solo_Fallecidos.pivot_table(index='Edad', values='Numero',aggfunc='count').reset_index()


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
              title='Contagiados por Sexo') 


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
              title='Contagiados por atención') 


figures_to_html([fig1])


def figures_to_html(figs, filename="Contagios_Edad.html"):
    Colombia_Covid = open(filename, 'w')
    Colombia_Covid.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        Colombia_Covid.write(inner_html)
    Colombia_Covid.write("</body></html>" + "\n")
    
     
    
fig1 = px.histogram(df, 
              x = 'Edad', 
              title='Contagiados por Edad')


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
              title='Fallecidos por Sexo')


figures_to_html([fig1])



def figures_to_html(figs, filename="Fallecidos_edad.html"):
    Colombia_Covid = open(filename, 'w')
    Colombia_Covid.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        Colombia_Covid.write(inner_html)
    Colombia_Covid.write("</body></html>" + "\n")
    
     
    
fig1 = px.histogram(Solo_Fallecidos, 
              x = 'Edad', 
              title='Fallecidos por Edad')


figures_to_html([fig1])



def figures_to_html(figs, filename="Atencion_pacientes.html"):
    Colombia_Covid = open(filename, 'w')
    Colombia_Covid.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        Colombia_Covid.write(inner_html)
    Colombia_Covid.write("</body></html>" + "\n")
    
     
    
fig1 = px.pie(df, 
              values='Numero', 
              names='atención', 
              title='Atención pacientes')


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
                    colorbar_title="Contagiados en Colombia"))
fig1.update_layout(mapbox_style="carto-positron",
                        mapbox_zoom=3.7,
                        mapbox_center = {"lat": 4.570868, "lon": -74.2973328},
                 title_text = 'Contagiados en Colombia')


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
                    colorbar_title="Muertes en Colombia"))
fig1.update_layout(mapbox_style="carto-positron",
                        mapbox_zoom=3.7,
                        mapbox_center = {"lat": 4.570868, "lon": -74.2973328},
                 title_text = 'Muertes en Colombia')


figures_to_html([fig1])





