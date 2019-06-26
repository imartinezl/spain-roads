#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 20:36:19 2019

@author: imartinez
"""

# %%
import geopandas as gpd

border_file = 'ESP_adm/ESP_adm0.shp'
border = gpd.read_file( border_file)

file = 'data/RT_GIPUZKOA/RT_GIPUZKOA/RT_VIARIA/rt_tramo_vial.shp'
df = gpd.read_file( file )

# %%
df.clase.unique()
clase_selection = [1001, 1002, 1005, 1003]
column_selection = ['clase','geometry']
df_filter = df[df.clase.isin(clase_selection)][column_selection]
df_filter.geometry = df_filter.geometry.simplify(tolerance=1, preserve_topology=False)
df_filter.to_csv('test.csv')


# %%
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(15,9),facecolor=('black'))
df_filter.plot(column='clase', cmap='spring', alpha=0.1, ax = ax)
border.plot(edgecolor='white', lw=1, facecolor='#161616', ax = ax)
ax.set_xlim((-3,-1.5))
ax.set_ylim((42.8,43.5))
#ax.axis('equal')
ax.axis('off')



# %% reduce shapefiles

from pathlib import Path
import geopandas as gpd
import gc
import os

for filename in Path('data/raw').glob('**/rt_tramo_vial.shp'):
    print(filename)
    df = gpd.read_file( filename )
    clase_selection = [1001, 1002, 1005, 1003, 2000]
    column_selection = ['clase','geometry']
    df_filter = df[df.clase.isin(clase_selection)][column_selection]
    df_filter.geometry = df_filter.geometry.simplify(tolerance=1, preserve_topology=False)
    
    f_ = str(filename).split('/')
    folder = 'data/processed/' + f_[2] + '/'; os.mkdir(folder)
    df_filter.to_file(folder + f_[5])
    gc.collect()

# %% join all reduced shapefiles
    
from pathlib import Path
import geopandas as gpd
import pandas as pd
import gc
import os

df_list = []
for filename in Path('data/processed').glob('**/rt_tramo_vial.shp'):
    print(filename)
    df = gpd.read_file( filename )
    df_list.append(df)
    gc.collect()

df_total = pd.concat(df_list)
df_total.to_file('spain.shp')
