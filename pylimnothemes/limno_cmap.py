import matplotlib.pyplot as plt
import matplotlib as mpl
import cycler as cycler
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

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
