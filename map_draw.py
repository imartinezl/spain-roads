#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 23:58:22 2019

@author: imartinez
"""

from pathlib import Path
import geopandas as gpd
import matplotlib.pyplot as plt
import gc


#df_list = []
fig, ax = plt.subplots(figsize=(15,9),facecolor=('#161616'))
plt.tight_layout()
ax.axis('off')
#border.plot(edgecolor='white', lw=1, facecolor='#161616', ax = ax)

for filename in Path('data').glob('**/rt_tramo_vial.shp'):
    print(filename)
    df = gpd.read_file( filename )
    clase_selection = [1001, 1002, 1005, 1003]
    column_selection = ['clase','geometry']
    df_filter = df[df.clase.isin(clase_selection)][column_selection]
    df_filter.loc[df_filter.clase==1005, 'clase'] = 1003
    df_filter.geometry = df_filter.geometry.simplify(tolerance=1, preserve_topology=False)
    df_filter.plot(column='clase', cmap='cool', alpha=0.1, ax = ax)
    gc.collect()
    
plt.savefig('hey.png', facecolor=('#161616'), dpi=300 )
