import matplotlib.pyplot as plt
import matplotlib as mpl
import cycler as cycler
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

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