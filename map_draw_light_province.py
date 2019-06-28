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



for filename in Path('data/raw').glob('**/rt_tramo_vial.shp'):
    print(filename, str(round(os.path.getsize(filename)/1e6,2))+ "MB")
    df = gpd.read_file( filename )
    fig, ax = plt.subplots(figsize=(26,15),facecolor=('white'))
    plt.tight_layout()
    df.plot(color='black', lw=1, alpha=0.2, ax = ax)
    ax.axis('off')
    ax.set_aspect('equal')
    plt.savefig(str(filename).split('/')[2] + '.png', facecolor=('white'), dpi=100 )
    plt.close()
    gc.collect()




