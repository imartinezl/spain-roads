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
from cartopy import crs as ccrs
crs = ccrs.Orthographic(central_longitude=-5, central_latitude=40)
crs_proj4 = crs.proj4_init
fig, ax = plt.subplots(figsize=(12,10), facecolor=('#181818'))
plt.tight_layout()

border_file = 'ESP_adm/ESP_adm0.shp'
border = gpd.read_file( border_file).to_crs(crs_proj4)
ax = border.plot(color='#000000', lw=1, alpha=1, ax=ax)
                 
prefix = 'data/processed/'
suffix = '/rt_tramo_vial.shp'

m = ["RT_PONTEVEDRA","RT_VALLADOLID","RT_BURGOS","RT_SEGOVIA","RT_BARCELONA",
     "RT_NAVARRA","RT_GRANADA","RT_GIRONA","RT_ZARAGOZA",#"RT_LAS_PALMAS",
     "RT_GUADALAJARA","RT_HUELVA","RT_SORIA","RT_A_CORUNA","RT_ALBACETE",
     "RT_MADRID","RT_MURCIA","RT_ZAMORA","RT_PALENCIA","RT_VALENCIA","RT_TARRAGONA",
     "RT_ALMERIA","RT_CIUDAD_REAL","RT_BADAJOZ","RT_TOLEDO","RT_LA_RIOJA",
     "RT_CACERES","RT_MALAGA","RT_ILLES_BALEARS","RT_LUGO","RT_CORDOBA","RT_CUENCA",
     "RT_GIPUZKOA","RT_AVILA","RT_JAEN","RT_OURENSE",#"RT_SANTA_CRUZ_DE_TENERIFE",
     "RT_LLEIDA","RT_CEUTA","RT_ARABA_ALAVA","RT_SALAMANCA","RT_MELILLA","RT_CADIZ",
     "RT_TERUEL","RT_CASTELLON_CASTELLO","RT_ALICANTE_ALACANT","RT_BIZKAIA",
     "RT_HUESCA","RT_SEVILLA","RT_ASTURIAS","RT_LEON","RT_CANTABRIA"]
m = ["RT_PONTEVEDRA","RT_VALLADOLID","RT_BURGOS","RT_SEGOVIA","RT_BARCELONA",
     "RT_NAVARRA","RT_GIRONA","RT_ZARAGOZA",
     "RT_GUADALAJARA","RT_SORIA","RT_A_CORUNA",
     "RT_MADRID","RT_ZAMORA","RT_PALENCIA","RT_TARRAGONA","RT_LA_RIOJA",
     "RT_LUGO","RT_CUENCA", "RT_GIPUZKOA","RT_AVILA","RT_OURENSE",
     "RT_LLEIDA","RT_ARABA_ALAVA","RT_SALAMANCA",
     "RT_TERUEL","RT_CASTELLON_CASTELLO","RT_BIZKAIA",
     "RT_HUESCA","RT_ASTURIAS","RT_LEON","RT_CANTABRIA"]
m = ["RT_GRANADA","RT_GUADALAJARA","RT_HUELVA","RT_ALBACETE",
     "RT_MADRID","RT_MURCIA","RT_VALENCIA",
     "RT_ALMERIA","RT_CIUDAD_REAL","RT_BADAJOZ","RT_TOLEDO",
     "RT_CACERES","RT_MALAGA","RT_ILLES_BALEARS","RT_CORDOBA","RT_CUENCA",
     "RT_AVILA","RT_JAEN","RT_CEUTA","RT_SALAMANCA","RT_MELILLA","RT_CADIZ",
     "RT_TERUEL","RT_CASTELLON_CASTELLO","RT_ALICANTE_ALACANT","RT_SEVILLA"]
[prefix + x + suffix for x in m]
                 
#for filename in Path('data/processed').glob('**/rt_tramo_vial.shp'):
for filename in [prefix + x + suffix for x in m]:
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


