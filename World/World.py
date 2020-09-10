#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 12:12:00 2020

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
from datetime import date, timedelta
from datetime import time
from datetime import datetime


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output



#####################################
#Data

df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
date_string = df['date']
#date_object = date_string.strptime('%Y,-%m')
#date_object = datetime.strptime(date_string, '%Y-%m')
df ['Year'] = df['date'].apply(lambda t: t.split('-')[0])
df ['Month'] = df['date'].apply(lambda t: t.split('-')[1])
df ['Year - Month'] = df ['Year'] + '-' + df ['Month']

#### Fecha

yesterday = date.today()-timedelta(days=1)
#yesterday = date.today()
fecha = yesterday.strftime("%Y-%m-%d")

#today = date.today()
#fecha = today.strftime("%Y-%m-%d")

otro = df['date'] == fecha
otro2 = df[otro]
with_world = otro2['location'] != 'World'

with_int1 = otro2[with_world]
with_int2 = with_int1['location'] != 'International'
actual = with_int1[with_int2]


### reemplazar valores nuos con 0

#actual = actual.fillna(0)


df_order_total_cases = actual.sort_values('total_cases',ascending=False)
#df_order_total_cases.head()

df_order_total_death = actual.sort_values('total_deaths',ascending=False)
#df_order_total_death.head()

uno = (df['location'] != 'World') & (df['continent'] != 'International')
uno2 = df[uno]

uno3 = uno2['location'] != 'International'
uno4 = uno2[uno3]

sud = df['continent'] =='South America'
sudamerica = df[sud]

uno = (df['location'] != 'World') & (df['continent'] != 'International')
uno2 = df[uno]

uno3 = uno2['location'] != 'International'
uno4 = uno2[uno3]

uno5 = sudamerica['date'] == fecha
subamerica_hoy = sudamerica[uno5]

Wd = df['location'] == 'World'
World = df[Wd]


df_order_total_cases_per_mill = actual.sort_values('total_cases_per_million',ascending=False)
df_order_total_deaths_per_mill = actual.sort_values('total_deaths_per_million',ascending=False)


##### creación de graficas


def figures_to_html(figs, filename="20paisescontagios.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
fig1 = px.bar(df_order_total_cases.head(20), x = 'location', y = 'total_cases', barmode='relative') 
   

figures_to_html([fig1])


def figures_to_html(figs, filename="20paisesmuertes.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
fig1 = px.bar(df_order_total_death.head(20), x = 'location', y = 'total_deaths', barmode='relative')


figures_to_html([fig1])


def figures_to_html(figs, filename="Continente_contagios.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
fig1 = px.pie(actual, values='total_cases', names='continent')


figures_to_html([fig1])


def figures_to_html(figs, filename="Continente_muertes.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
fig1 = px.pie(actual, values='total_deaths', names='continent')


figures_to_html([fig1])


def figures_to_html(figs, filename="Contagiados_Fecha_Paises.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
fig1 = px.line(df, x='date', y='total_cases', color='location')


figures_to_html([fig1])


def figures_to_html(figs, filename="fecha_Muertes_Paises.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
fig1 = px.line(df, x='date', y='total_deaths', color='location')


figures_to_html([fig1])


def figures_to_html(figs, filename="Numero_contagios_fecha.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
fig1 = px.line(World, x='date', y='total_cases')


figures_to_html([fig1])


def figures_to_html(figs, filename="Numero_muertes_fecha.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
fig1 = px.line(World, x='date', y='total_deaths')


figures_to_html([fig1])



def figures_to_html(figs, filename="Mapa_Mundo_contagios.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
data =  dict (type = 'choropleth',
             locations = actual['iso_code'],
             z = actual['total_cases'],
             text = actual['location'],
             colorbar = {'title': 'Contagiados'})


layout = dict (geo = dict (showframe = False, projection = {'type':'mercator'}))


choromap = go.Figure(data = [data], layout =layout) 


figures_to_html([choromap])



def figures_to_html(figs, filename="Mapa_Mundo_muertes.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
data2 =  dict (type = 'choropleth',
             locations = actual['iso_code'],
             z = actual['total_deaths'],
             text = actual['location'],
             colorbar = {'title': 'Muertes'})

layout2 = dict (geo = dict (showframe = False, projection = {'type':'mercator'}))

choromap2 = go.Figure(data = [data2], layout =layout2)


figures_to_html([choromap2])


def figures_to_html(figs, filename="Tabla_contagiados_fallecidos.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
    
Today = date.today()
fecha2 = Today.strftime("%Y-%m-%d")

otro = df['date'] == fecha2
otro2 = df[otro]

Only_world1 = otro2['location'] == 'World'
Only_world2 = otro2[Only_world1]

#Contagi = actual['total_cases'].sum()
Contagi = Only_world2['total_cases'].sum()

Total_deaths = Only_world2['total_deaths'].sum()

total_res_wor = pd.DataFrame({'Contagiados': [Contagi],'Fallecidos': [Total_deaths], 'Fecha':[fecha2]})

fig1 = go.Figure(data=[go.Table(
    header=dict(values=list(total_res_wor.columns),
                fill_color='rgba(15, 78, 64, 0.1)',
                align='center'),
    cells=dict(values=[total_res_wor.Contagiados, total_res_wor.Fallecidos, total_res_wor.Fecha ],
               fill_color='rgba(255, 255, 255, 0.1)',
               align='center',
               format = [",.0f", ",.0f",None]))
])




figures_to_html([fig1])

yesterday = date.today()-timedelta(days=1)
#yesterday = date.today()
fecha = yesterday.strftime("%Y-%m-%d")

otro = df['date'] == fecha
otro2 = df[otro]
with_world = otro2['location'] != 'World'

with_int1 = otro2[with_world]
with_int2 = with_int1['location'] != 'International'
actual = with_int1[with_int2]



def figures_to_html(figs, filename="Cases_per_millon.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
    
fig1 = px.bar(df_order_total_cases_per_mill.head(20), x = 'location', y = 'total_cases_per_million')


figures_to_html([fig1])



def figures_to_html(figs, filename="deaths_per_millon.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
    
fig1 = px.bar(df_order_total_deaths_per_mill.head(20), x = 'location', y = 'total_deaths_per_million')

figures_to_html([fig1])


def figures_to_html(figs, filename="deaths_extreme_poverty.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
    
fig1 = px.scatter(actual, x="extreme_poverty", y="total_deaths", color = "continent")

figures_to_html([fig1])




def figures_to_html(figs, filename="cardiovasc_death_rate.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
    
fig1 = px.scatter(actual, x="cardiovasc_death_rate", y="total_deaths", color = "continent")

figures_to_html([fig1])


def figures_to_html(figs, filename="diabetes_prevalence.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
    
fig1 = px.scatter(actual, x="diabetes_prevalence", y="total_deaths", color = "continent")

figures_to_html([fig1])




def figures_to_html(figs, filename="New_cases_per_millon.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
    

df_order_new_cases_per_mill = actual.sort_values('new_cases_per_million',ascending=False)

fig1 = px.bar(df_order_new_cases_per_mill.head(20), x = 'location', y = 'new_cases_per_million')



figures_to_html([fig1])



def figures_to_html(figs, filename="New_deaths_per_millon.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
    

df_order_new_deaths_per_mill = actual.sort_values('new_deaths_per_million',ascending=False)

fig1 = px.bar(df_order_new_deaths_per_mill.head(20), x = 'location', y = 'new_deaths_per_million')


figures_to_html([fig1])






