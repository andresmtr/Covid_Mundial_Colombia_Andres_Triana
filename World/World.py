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
fecha = yesterday.strftime("%Y-%m-%d")

#today = date.today()
#fecha = today.strftime("%Y-%m-%d")

otro = df['date'] == fecha
otro2 = df[otro]
with_world = otro2['location'] != 'World'
actual = otro2[with_world]


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


##### creación de graficas




def figures_to_html(figs, filename="20paisescontagios.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
fig1 = px.bar(df_order_total_cases.head(20), x = 'location', y = 'total_cases', barmode='relative', title='20 paises con más casos confirmados') 
   

figures_to_html([fig1])


def figures_to_html(figs, filename="20paisesmuertes.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
fig1 = px.bar(df_order_total_death.head(20), x = 'location', y = 'total_deaths', barmode='relative', title='20 paises con más muertes confirmadas')


figures_to_html([fig1])


def figures_to_html(figs, filename="Continente_contagios.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
fig1 = px.pie(actual, values='total_cases', names='continent', title='Continente con más casos')


figures_to_html([fig1])


def figures_to_html(figs, filename="Continente_muertes.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
fig1 = px.pie(actual, values='total_deaths', names='continent', title='Continente con más muertes')


figures_to_html([fig1])


def figures_to_html(figs, filename="Contagiados_Fecha_Paises.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
fig1 = px.line(df, x='date', y='total_cases', color='location', title='Contagiados por fecha')


figures_to_html([fig1])


def figures_to_html(figs, filename="fecha_Muertes_Paises.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
fig1 = px.line(df, x='date', y='total_deaths', color='location', title='Muertes por fecha')


figures_to_html([fig1])


def figures_to_html(figs, filename="Numero_contagios_fecha.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
fig1 = px.line(World, x='date', y='total_cases', title='Contagiados por fecha')


figures_to_html([fig1])


def figures_to_html(figs, filename="Numero_muertes_fecha.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")
    
fig1 = px.line(World, x='date', y='total_deaths', title='Muertes por fecha')


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
             colorbar = {'title': 'Casos confirmados por país'})


layout = dict (title = 'Casos confirmados por país',
              geo = dict (showframe = False, projection = {'type':'mercator'}))


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
             colorbar = {'title': 'Muertes confirmadas por país'})

layout2 = dict (title = 'Muertes confirmadas por país',
              geo = dict (showframe = False, projection = {'type':'mercator'}))

choromap2 = go.Figure(data = [data2], layout =layout2)


figures_to_html([choromap2])





