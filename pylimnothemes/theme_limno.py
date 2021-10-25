import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
from .limno_pal import limno_pal
from .limno_cols import limno_cols


def theme_limno(palette='main', reverse=False):

	# font
	mpl.rcParams['font.family'] = 'sans-serif'
	mpl.rcParams['font.sans-serif'] = ['Calibri']

	# font colors
	mpl.rcParams['axes.titlecolor'] = '#4D4D4D'
	mpl.rcParams['xtick.color'] = '#999999'
	mpl.rcParams['xtick.labelcolor'] = '#999999'
	mpl.rcParams['ytick.labelcolor'] = '#999999'
	mpl.rcParams['ytick.color'] = '#999999'
	mpl.rcParams['axes.labelcolor'] = '#999999'
	mpl.rcParams['text.color'] = '#999999'

	# background color
	mpl.rcParams["figure.facecolor"] = 'white'
	mpl.rcParams["axes.facecolor"] = 'white'
	mpl.rcParams["savefig.facecolor"] = 'white'

	# spine color 
	mpl. rcParams['axes.edgecolor']  = '#999999'

	# set color palette
	cpal = limno_pal(palette, reverse=reverse)
	mpl.rcParams['axes.prop_cycle'] = cycler(color=cpal)