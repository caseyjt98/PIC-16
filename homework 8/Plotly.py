#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 14:50:56 2018

@author: caseytaylor
"""

import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tools
import itertools

# Embed Plotly plot in an IPython notebook:
tools.embed('dfreder1', '69')

dfreder1 = py.get_figure('dfreder1', '69')
# print(dfreder1.to_string())

# get data object
years = dfreder1.get_data()[0]['x'] 

unique_years = list(set(years))

# get number of bridges per year
dictionary = {year:years.count(year) for year in unique_years}

# delete pair u'(21658': 1
dictionary2 = {i:dictionary[i] for i in dictionary if i!=u'(21658'}
unique_years2 = [i for i in unique_years if i!= u'(21658']

cumulative_bridges = []
bridges = 0 
for x in dictionary2:
    bridges = bridges + dictionary2[x] # update cumulative bridge value
    cumulative_bridges.append(bridges) # append to list
# print cumulative_bridges

data = dict(itertools.izip(unique_years2, cumulative_bridges))

# Create a trace
trace = go.Scatter(
    x = data.keys(),
    y = data.values(),
    fill = 'tozeroy',
    marker= dict(
        color=u'rgb(255, 127, 14)'
    ),
    mode = 'lines'
)

data = [trace]

layout = go.Layout(
    autosize=False,
    width=600,
    height=400,
    title='Total Bridges Built in CA since 1900',
        titlefont=dict(
            family='Times New Roman'
        ),
    xaxis=dict(
        title='Years',
        dtick=10,
        range = [1900,2013],
        titlefont=dict(
            family='Times New Roman, monospace',
            size=18,
            color='black'
        ),
         tickfont=dict(
            family='Times New Roman',
        )
    ),
    yaxis=dict(
        title='Cumulative Bridges',
        dtick=5000,
        titlefont=dict(
            family='Times New Roman, monospace',
            size=18,
            color='black'
        ),
        tickfont=dict(
            family='Times New Roman',
        )
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='assignment 8')

# default resolution is 600, 400
# set resolution to 1800, 1500 using scale of 3
py.image.save_as(fig,"scatter.png",scale = 3)
py.image.ishow(fig)