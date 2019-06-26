#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 23:58:22 2019

@author: imartinez
"""

from pathlib import Path
import os
import geopandas as gpd
import matplotlib.pyplot as plt
import gc


#df_list = []
fig, ax = plt.subplots(figsize=(26,15),facecolor=('white'))
plt.tight_layout()
ax.axis('off')
#border.plot(edgecolor='white', lw=1, facecolor='#161616', ax = ax)

for filename in Path('data').glob('**/rt_tramo_vial.shp'):
    print(filename, str(round(os.path.getsize(filename)/1e6,2))+ "MB")
    df = gpd.read_file( filename )
    clase_selection = [1001, 1002, 1005, 1003, 2000]
    column_selection = ['clase','geometry']
    df_filter = df[df.clase.isin(clase_selection)][column_selection]
    df_filter.loc[df_filter.clase==1005, 'clase'] = 1003
    df_filter.geometry = df_filter.geometry.simplify(tolerance=1, preserve_topology=False)
    df_filter.plot(color='black', lw=1, alpha=0.08, ax = ax)
    gc.collect()

plt.axis('equal') 
ax.set_aspect('equal')   
plt.savefig('hey.png', facecolor=('white'), dpi=100 )


