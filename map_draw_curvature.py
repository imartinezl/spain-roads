#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 14:23:34 2019

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

for filename in Path('data/raw').glob('**/rt_tramo_vial.shp'):
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


# %%
border_file = 'ESP_adm/ESP_adm0.shp'
border = gpd.read_file( border_file)
border.plot(color='black', lw=1)

# Define the CartoPy CRS object.
from cartopy import crs as ccrs
crs = ccrs.NearsidePerspective(
        central_longitude=-5, 
        central_latitude=40, 
        satellite_height=35785831/200)


# This can be converted into a `proj4` string/dict compatible with GeoPandas
crs_proj4 = crs.proj4_init
border_ae = border.to_crs(crs_proj4)
df_ae = df.to_crs(crs_proj4)

# Here's what the plot looks like in GeoPandas
border.plot()
border_ae.plot()
plt.plot(df)

fig, ax = plt.subplots(figsize=(16,9), subplot_kw={'projection': crs})
ax.add_geometries(border_ae['geometry'], crs=crs)

from shapely.geometry import Point, LineString, shape
import pandas as pd
X = [-10, -5]
Y = [40, 40]
line_id = [0, 0]
df = pd.DataFrame([line_id,X,Y]).transpose(); df.columns = ['line_id','X','Y']
geometry = [Point(xy) for xy in zip(df.X,df.Y)]
geo_df = gpd.GeoDataFrame(df, geometry=geometry)
df = df.groupby(['line_id'])['geometry'].apply(lambda x: LineString(x.tolist()))
df = gpd.GeoDataFrame(df, geometry='geometry')
df.crs = {'init': 'epsg:4326', 'no_defs': True}
df.plot()

# %%
filename = 'data/RT_ARABA_ALAVA/RT_ARABA_ALAVA/RT_VIARIA/rt_tramo_vial.shp'
df = gpd.read_file( filename )
clase_selection = [1001, 1002, 1005, 1003, 2000]
column_selection = ['clase','geometry']
df_filter = df[df.clase.isin(clase_selection)][column_selection]
df_filter.loc[df_filter.clase==1005, 'clase'] = 1003
df_filter.geometry = df_filter.geometry.simplify(tolerance=1, preserve_topology=False)
df_filter.plot(color='black', lw=1, alpha=0.08)
