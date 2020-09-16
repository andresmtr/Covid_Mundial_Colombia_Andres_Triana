#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:48:07 2020

@author: andresmauriciotrianareina
"""


######################################################
#### Importar datos
#####################################################


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
import plotly.offline as pyo
import time
from datetime import date, timedelta

######################################################
#### Llamar coordenadas del mapa
#####################################################

import json
from urllib.request import urlopen
with urlopen('https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/be6a6e239cd5b5b803c6e7c2ec405b793a9064dd/Colombia.geo.json') as response:
    counties = json.load(response)
    

######################################################
#### Llamar base de datos
#####################################################
    

import requests

url = 'https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD&bom=true&format=true'

myfile = requests.get(url)


open('/Users/andresmauriciotrianareina/Documents/Cursos_desarrollo/Data_science/My_excercise/0_prueba/Casos_positivos_de_COVID-19_en_Colombia.csv', 'wb').write(myfile.content)


df = pd.read_csv('/Users/andresmauriciotrianareina/Documents/Cursos_desarrollo/Data_science/My_excercise/0_prueba/Casos_positivos_de_COVID-19_en_Colombia.csv')


######################################################
#### Limpiar datos
#####################################################

########################
#### crear fecha


df ['Fecha identificación'] = df['fecha reporte web'].apply(lambda t: t.split('T')[0])

df['Numero'] = 1

df['Lugar'] = df['Departamento o Distrito ']

########################
#### nombre departamentos

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

########################
#### sexo


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

df['Sexo'].replace(
    to_replace=['M'],
    value='Masculino',
    inplace=True
)

df['Sexo'].replace(
    to_replace=['F'],
    value='Femenino',
    inplace=True
)


########################
#### atención

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


######################################################
#### crear frame principales
#####################################################

########################
#### Contagios sexo


Sexo = df.pivot_table(index='Sexo', values='Numero',aggfunc='count').reset_index()

Sexo_m = Sexo[Sexo['Sexo']=='Masculino']
Sexo_f = Sexo[Sexo['Sexo']=='Femenino']

fig = go.Figure()
fig.add_trace(go.Bar(x=Sexo_m['Sexo'],
                y=Sexo_m['Numero'],
                name='Masculino',
                marker_color='rgb(55, 83, 109)'
                ))
fig.add_trace(go.Bar(x=Sexo_f['Sexo'],
                y=Sexo_f['Numero'],
                name='Femenino',
                marker_color='rgb(26, 118, 255)'
                ))

fig.update_traces(
        texttemplate='%{y:.2s}', 
        textposition='outside')

fig.update_layout(
    title='Contagios por Sexo',
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='Cantidad',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(
        x=0.8,
        y=1.1,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

pyo.plot(fig, filename = 'Contagios_sexo.html')


########################
#### atención contagiados

Atención = df.pivot_table(index='atención', values='Numero',aggfunc='count').reset_index()

Atención_casa = Atención[Atención['atención'] == 'Casa']
Atención_Fallecido = Atención[Atención['atención'] == 'Fallecido']
Atención_Hospital = Atención[Atención['atención'] == 'Hospital']
Atención_Hospital_UCI = Atención[Atención['atención'] == 'Hospital UCI']
Atención_Recuperado = Atención[Atención['atención'] == 'Recuperado']


fig = go.Figure()
fig.add_trace(go.Bar(x=Atención_casa['atención'],
                y=Atención_casa['Numero'],
                name='Casa',
                marker_color='rgb(55, 83, 109)'
                ))
fig.add_trace(go.Bar(x=Atención_Fallecido['atención'],
                y=Atención_Fallecido['Numero'],
                name='Fallecidos',
                marker_color='rgb(26, 118, 255)'
                ))

fig.add_trace(go.Bar(x=Atención_Hospital['atención'],
                y=Atención_Hospital['Numero'],
                name='Hospital',
                marker_color='rgb(132, 181, 159)'
                ))

fig.add_trace(go.Bar(x=Atención_Hospital_UCI['atención'],
                y=Atención_Hospital_UCI['Numero'],
                name='Hospital UCI',
                marker_color='rgb(163, 201, 168)'
                ))

fig.add_trace(go.Bar(x=Atención_Recuperado['atención'],
                y=Atención_Recuperado['Numero'],
                name='Recuperado',
                marker_color='rgb(221, 216, 196)'
                ))

fig.update_traces(
        texttemplate='%{y:.2s}', 
        textposition='outside')

fig.update_layout(
    title='Antención contagiados',
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='Cantidad',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(
        x=0,
        y=1,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

pyo.plot(fig, filename = 'Atención_contagiados.html')


########################
#### Contagios por Edad


fig = go.Figure(data=[go.Histogram(x=df['Edad'], marker_color='rgb(55, 83, 109)')])

fig.update_layout(
    title='Edad contagiados',
    xaxis_tickfont_size=14,
    xaxis_title_text='Edad',
    yaxis=dict(
        title='Cantidad',
        titlefont_size=16,
        tickfont_size=14,
    ),

)
pyo.plot(fig, filename = 'Contagios_Edad.html')

########################
#### Fallecidos sexo

Solo_Fallecidos = df[df['atención'] == 'Fallecido']


Solo_Fallecidos ['Fecha de muerte f'] = Solo_Fallecidos['Fecha de muerte'].apply(lambda t: t.split('T')[0])

Sexo_fallecidos = Solo_Fallecidos.pivot_table(index='Sexo', values='Numero',aggfunc='count').reset_index()

Fallecidos_Sexo_m = Sexo_fallecidos[Sexo_fallecidos['Sexo']=='Masculino']
Fallecidos_Sexo_f = Sexo_fallecidos[Sexo_fallecidos['Sexo']=='Femenino']

fig = go.Figure()
fig.add_trace(go.Bar(x=Fallecidos_Sexo_m['Sexo'],
                y=Fallecidos_Sexo_m['Numero'],
                name='Masculino',
                marker_color='rgb(55, 83, 109)'
                ))
fig.add_trace(go.Bar(x=Fallecidos_Sexo_f['Sexo'],
                y=Fallecidos_Sexo_f['Numero'],
                name='Femenino',
                marker_color='rgb(26, 118, 255)'
                ))

fig.update_traces(
        texttemplate='%{y:.2s}', 
        textposition='outside')

fig.update_layout(
    title='Fallecidos por Sexo',
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='Cantidad',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(
        x=0.8,
        y=1.1,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

pyo.plot(fig, filename = 'Fallecidos_edad.html')



########################
#### Fallecidos edad


fig = go.Figure(data=[go.Histogram(x=Solo_Fallecidos['Edad'], marker_color='rgb(55, 83, 109)')])

fig.update_layout(
    title='Edad fallecidos',
    xaxis_tickfont_size=14,
    xaxis_title_text='Edad',
    yaxis=dict(
        title='Cantidad',
        titlefont_size=16,
        tickfont_size=14,
    ),

)
pyo.plot(fig, filename = 'Fallecidos_edad.html')


########################
#### Mapa contagiados

suma_casos_zona = df.groupby( ['Lugar'] ).sum().reset_index()

locs = suma_casos_zona['Lugar']

for loc in counties['features']:
    loc['id'] = loc['properties']['NOMBRE_DPT']
fig = go.Figure(go.Choroplethmapbox(
                    geojson=counties,
                    locations=locs,
                    z=suma_casos_zona['Numero'],
                    colorscale='Viridis',
                    colorbar_title="Contagiados"))
fig.update_layout(mapbox_style="carto-positron",
                        mapbox_zoom=3.4,
                        mapbox_center = {"lat": 4.570868, "lon": -74.2973328})

pyo.plot(fig, filename = 'Mapa_Contagiados.html')

########################
#### Mapa muerte

Suma_Solo_Fallecidos = Solo_Fallecidos.groupby( ['Lugar'] ).sum().reset_index()

locs2 = Suma_Solo_Fallecidos['Lugar']


for loc in counties['features']:
    loc['id'] = loc['properties']['NOMBRE_DPT']
fig = go.Figure(go.Choroplethmapbox(
                    geojson=counties,
                    locations=locs2,
                    z=Suma_Solo_Fallecidos['Numero'],
                    colorscale='Viridis',
                    colorbar_title="Muertes"))
fig.update_layout(mapbox_style="carto-positron",
                        mapbox_zoom=3.4,
                        mapbox_center = {"lat": 4.570868, "lon": -74.2973328})


pyo.plot(fig, filename = 'Mapa_muertes.html')


########################
#### Fecha de contagio

Fecha = df.groupby(['Fecha identificación']).count().reset_index()

fig = go.Figure(data=go.Scatter(
        x=Fecha['Fecha identificación'], 
        y=Fecha['Numero'], 
        mode='lines+markers'))

fig.update_layout(
    title='Fecha contagios',
    xaxis_tickfont_size=14,
    xaxis_title_text='Fecha',
    yaxis=dict(
        title='Cantidad',
        titlefont_size=16,
        tickfont_size=14,
    ),

)

pyo.plot(fig, filename = 'Fecha_Contagio.html')


########################
#### Fecha de sexo

Fecha2 = df.groupby(['Fecha identificación', 'Sexo']).count().reset_index()

Fecha_M = Fecha2[Fecha2['Sexo']=='Masculino']
Fecha_f = Fecha2[Fecha2['Sexo']=='Femenino']


fig = go.Figure()
fig.add_trace(go.Scatter(x=Fecha_M['Fecha identificación'], y=Fecha_M['Numero'],
                    mode='lines',
                    name='Masculino'))
fig.add_trace(go.Scatter(x=Fecha_f['Fecha identificación'], y=Fecha_f['Numero'],
                    mode='lines',
                    name='Femenino'))


fig.update_layout(
    title='Fecha contagios por sexo',
    xaxis_tickfont_size=14,
    xaxis_title_text='Fecha',
    yaxis=dict(
        title='Cantidad',
        titlefont_size=16,
        tickfont_size=14,
    ),

)

pyo.plot(fig, filename = 'Fecha_Contagio_sexo.html')


########################
#### tabla

total = df['Numero'].count()

muer1 = df[df['atención'] == 'Fallecido']

muer3 = muer1['Numero'].count()


Rec1 = df[df['atención'] == 'Recuperado']

Rec3 = Rec1['Numero'].count()


Today = date.today()-timedelta(days=1)
fecha2 = Today.strftime("%Y-%m-%d")

total_Fall = pd.DataFrame({'Contagiados': [total],'Fallecidos': [muer3], 'Recuperados':[Rec3], 'Fecha': [fecha2]})
                            
total_Fall  


fig = go.Figure(data=[go.Table(
    header=dict(values=list(total_Fall.columns),
                fill_color='rgba(15, 78, 64, 0.1)',
                align='center'),
    cells=dict(values=[total_Fall.Contagiados, total_Fall.Fallecidos, total_Fall.Recuperados,total_Fall.Fecha ],
               fill_color='rgba(255, 255, 255, 0.1)',
               align='center',
               format = [",.0f", ",.0f",",.0f",None]))
])



pyo.plot(fig, filename = 'Tabla_contagiados_fallecidos.html')


########################
#### Fallecidos por edad

Solo_fall_count = Solo_Fallecidos.groupby( ['Edad','Sexo'] ).sum().reset_index()

Solo_fall_count_M = Solo_fall_count[Solo_fall_count['Sexo']=='Masculino']
Solo_fall_count_f = Solo_fall_count[Solo_fall_count['Sexo']=='Femenino']


fig = go.Figure()
fig.add_trace(go.Scatter(x=Solo_fall_count_M['Edad'], y=Solo_fall_count_M['Numero'],
                    mode='markers',
                    name='Masculino',
                    marker_color='rgb(55, 83, 109)'))
fig.add_trace(go.Scatter(x=Solo_fall_count_f['Edad'], y=Solo_fall_count_f['Numero'],
                    mode='markers',
                    name='Femenino',
                    marker_color='rgb(26, 118, 255)'))


fig.update_layout(
    title='Fallecidos por sexo y edad',
    xaxis_tickfont_size=14,
    xaxis_title_text='Edad',
    yaxis=dict(
        title='Cantidad',
        titlefont_size=16,
        tickfont_size=14,
    ),

)
    
pyo.plot(fig, filename = 'Fallecidos_sexo_edad.html')


########################
#### Fallecidos por sexo




Fall_s = Solo_Fallecidos.pivot_table(index='Sexo', values='Numero',aggfunc='count').reset_index()

Fall_Sexo_m = Fall_s[Fall_s['Sexo']=='Masculino']
Fall_Sexo_f = Fall_s[Fall_s['Sexo']=='Femenino']

fig = go.Figure()
fig.add_trace(go.Bar(x=Fall_Sexo_m['Sexo'],
                y=Fall_Sexo_m['Numero'],
                name='Masculino',
                marker_color='rgb(55, 83, 109)'
                ))
fig.add_trace(go.Bar(x=Fall_Sexo_f['Sexo'],
                y=Fall_Sexo_f['Numero'],
                name='Femenino',
                marker_color='rgb(26, 118, 255)'
                ))

fig.update_traces(
        texttemplate='%{y:.2s}', 
        textposition='outside')

fig.update_layout(
    title='Fallcidos por Sexo',
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='Cantidad',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(
        x=0.8,
        y=1.1,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

pyo.plot(fig, filename = 'Fallecidos_Sexo.html')