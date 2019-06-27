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
from cartopy import crs as ccrs
crs = ccrs.Orthographic(central_longitude=-5, central_latitude=40)
crs_proj4 = crs.proj4_init
fig, ax = plt.subplots(figsize=(12,10), facecolor=('#181818'))
plt.tight_layout()

border_file = 'ESP_adm/ESP_adm0.shp'
border = gpd.read_file( border_file).to_crs(crs_proj4)
ax = border.plot(color='#000000', lw=1, alpha=1, ax=ax)
                 
                 
for filename in Path('data/processed').glob('**/rt_tramo_vial.shp'):
	print(filename, str(round(os.path.getsize(filename)/1e6,2))+ "MB")
	d = gpd.read_file( filename ).to_crs(crs_proj4)
	ax = d.plot(color='#00ffff', lw=0.5, alpha=0.1, ax=ax)
	ax = d.plot(color='#00ffff', lw=1, alpha=0.03, ax=ax)
	ax = d.plot(color='#00ffff', lw=2, alpha=0.015, ax=ax)
	gc.collect()
    
    
ax.set_facecolor('#181818')
#ax.set_xlim((-300000, 700000))
#ax.set_ylim((-500000, 500000))
ax.set_xlim((-400000, 800000))
ax.set_ylim((-500000, 500000))
ax.axis('off')
ax.set_aspect('equal')   
plt.savefig('hey.png', facecolor=('#181818'), dpi=400 )

# %%
border_file = 'ESP_adm/ESP_adm0.shp'
border = gpd.read_file( border_file)
border.plot(color='white', edgecolor='red',lw=1)

# Define the CartoPy CRS object.
from cartopy import crs as ccrs
crs = ccrs.NearsidePerspective(
        central_longitude=-5, 
        central_latitude=40, 
        satellite_height=35785831/200)
crs = ccrs.Orthographic(central_longitude=-5, central_latitude=40,)


# This can be converted into a `proj4` string/dict compatible with GeoPandas
crs_proj4 = crs.proj4_init
border_ae = border.to_crs(crs_proj4)

# Here's what the plot looks like in GeoPandas
border.plot()
border_ae.plot()

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
filename = 'data/spain.shp'
df = gpd.read_file( filename )
df_nourban = df[df.clase != 2000]

border_file = 'ESP_adm/ESP_adm0.shp'
border = gpd.read_file( border_file)
# %%
from cartopy import crs as ccrs
crs = ccrs.Orthographic(central_longitude=-5, central_latitude=40)
crs_proj4 = crs.proj4_init
fig, ax = plt.subplots(figsize=(12,10), facecolor=('#181818'))
d = df_nourban.to_crs(crs_proj4)
e =  border.to_crs(crs_proj4)

ax = e.plot(color='#000000', lw=1, alpha=1, ax=ax)
ax = d.plot(color='#00ffff', lw=1, alpha=0.11, ax=ax)
ax = d.plot(color='#00ffff', lw=2.5, alpha=0.02, ax=ax)
ax = d.plot(color='#00ffff', lw=5, alpha=0.015, ax=ax)
ax.set_facecolor('#181818')
#ax.set_xlim((-300000, 700000))
#ax.set_ylim((-500000, 500000))
ax.set_xlim((-400000, 800000))
ax.set_ylim((-500000, 500000))
ax.axis('off')
ax.set_aspect('equal')   
plt.savefig('hey.png', facecolor=('#181818'), dpi=400 )



