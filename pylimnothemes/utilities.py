import matplotlib.pyplot as plt
import matplotlib as mpl
import cycler as cycler
from matplotlib.colors import LinearSegmentedColormap
import numpy as np


def limno_cols(ls = []):
	limno_colors = {
		'limno_navy': '#174A7C',
		'limno_blue': '#174A7C',
		'limno_lightblue': '#56A0D3',
		'limno_cornflower': '#56A0D3',
		'limno_hunter': '#4A6D4D',
		'limno_moss': '#6B916E',
		'limno_lightgreen': '#94C197',
		'limno_purple': '#6A1148',
		'limno_red': '#DF4D4D',
		'limno_pink': '#ffa399',
		'limno_marigold': '#FFA552',
		'limno_yellow': '#94C197',
		'limno_silver': '#C7C7C7',
		'limno_platinum': '#E5E5E5'
	}

	if len(ls) == 0:
		return limno_colors
	else:
		limno_colors_reduced = {k: limno_colors[k] for k in ls}
		return [value for key, value in limno_colors_reduced.items()]

def reverse_colourmap(cmap, name = 'my_cmap_r'):
    """
    In: 
    cmap, name 
    Out:
    my_cmap_r

    Explanation:
    t[0] goes from 0 to 1
    row i:   x  y0  y1 -> t[0] t[1] t[2]
                   /
                  /
    row i+1: x  y0  y1 -> t[n] t[1] t[2]

    so the inverse should do the same:
    row i+1: x  y1  y0 -> 1-t[0] t[2] t[1]
                   /
                  /
    row i:   x  y1  y0 -> 1-t[n] t[2] t[1]\
    https://stackoverflow.com/questions/3279560/reverse-colormap-in-matplotlib
    """        
    reverse = []
    k = []   

    for key in cmap._segmentdata:    
        k.append(key)
        channel = cmap._segmentdata[key]
        data = []

        for t in channel:                    
            data.append((1-t[0],t[2],t[1]))            
        reverse.append(sorted(data))    

    LinearL = dict(zip(k,reverse))
    my_cmap_r = mpl.colors.LinearSegmentedColormap(name, LinearL) 
    return my_cmap_r


def limno_pal(palette='main', reverse = False):
	limno_palettes = {
		'main': limno_cols(['limno_lightblue', 'limno_lightgreen', 'limno_red', 
                           'limno_navy', 'limno_hunter', 'limno_purple']),
		'secondary': limno_cols(['limno_cornflower', 'limno_moss', 'limno_pink',
                           'limno_marigold', 'limno_yellow', 'limno_silver'])
	}

	pal = limno_palettes[palette]
	if reverse == True:
		pal = pal.reverse()

	return pal


def limno_cmap(cmap='All', reverse=False):
	limno_colormap_lists = {
		'limno_blues': ['#174A7C','#366B9A','#558BB7','#74ABD4','#93CBF1'],
		'limno_greens': ['#426144', '#577959', '#6B916E', '#80A983', '#94C197'],
		'limno_reds': ['#6A1148', '#A52F4B', '#DF4D4D', '#EF7873', '#FFA299'],
		'limno_greys':['#313131', '#5E5E5E', '#8B8B8B', '#B8B8B8', '#E5E5E5'],
		'limno_RdYlGn_lite': ['#DF4D4D', '#FFA552', '#FFA552', '#C5E0B4', '#E2F0D9'],
		'limno_RdYlGn_dark': ['#DF4D4D', '#FFA552', '#FFA552', '#94C197', '#426144'],
	}
    
	if reverse == True:
		for key in limno_colormap_lists.keys():
			limno_colormap_lists[key] = limno_colormap_lists[key][::-1]
    
	limno_colormaps = {}

	for key in limno_colormap_lists:
		limno_colormaps[key] = LinearSegmentedColormap.from_list('custom', limno_colormap_lists[key], N=256)

	if cmap == 'All': 
		return limno_colormaps
	else:
		try:
			cmap = limno_colormaps[cmap]
			return cmap
		except:
			print("Not a LimnoTech color palette. Please select from the following: ", [f for f in limno_colormap_lists.keys()])


def theme_limno(palette='main'):
	# color palette 
	mpl.rcParams['axes.prop_cycle'] = cycler(color=limno_pal(palette))

	# font
	mpl.rcParams['font.family'] = 'sans-serif'
	mpl.rcParams['font.sans-serif'] = ['Calibri']
	mpl.rcParams['axes.titlecolor'] = '#4D4D4D'
	mpl.rcParams['xtick.color'] = '#999999'
	mpl.rcParams['xtick.labelcolor'] = '#999999'
	mpl.rcParams['ytick.labelcolor'] = '#999999'
	mpl.rcParams['ytick.color'] = '#999999'
    
    
my_cmap = limno_cmap('limno_reds')
my_cmap_r = limno_cmap('limno_reds', reverse=True)
my_cmap_bl = limno_cmap('limno_blues')
my_cmap_div = limno_cmap('limno_RdYlGn_dark')