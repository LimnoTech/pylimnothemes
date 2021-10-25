import matplotlib.pyplot as plt
import matplotlib as mpl
import cycler as cycler
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
from .limno_pal import limno_pal
from .limno_cols import limno_cols


def theme_limno(palette='main'):

	# font
	mpl.rcParams['font.family'] = 'sans-serif'
	mpl.rcParams['font.sans-serif'] = ['Calibri']
	mpl.rcParams['axes.titlecolor'] = '#4D4D4D'
	mpl.rcParams['xtick.color'] = '#999999'
	mpl.rcParams['xtick.labelcolor'] = '#999999'
	mpl.rcParams['ytick.labelcolor'] = '#999999'
	mpl.rcParams['ytick.color'] = '#999999'

	print('the palette is %s' % palette)
	cpal = limno_pal(palette)
	print(cpal)


    # color palette 
	mpl.rcParams['axes.prop_cycle'] = cycler(color=limno_pal(palette))