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