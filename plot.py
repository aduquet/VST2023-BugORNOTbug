import pandas as pd
import numpy as np
import glob as gl
import pickle
from efficient_apriori import apriori
import matplotlib.pyplot as plt

import warnings
import os
import pathlib

import seaborn as sns
import statsmodels.api as sm
import scipy.stats as stats
warnings.filterwarnings('ignore')
from matplotlib import rc

rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('font',**{'family':'serif','serif':['Times']})
rc('text', usetex=True)
plt.rcParams.update({'font.size': 14})

X = ['0','1','2','3', '4', '5', '6', '7', '8', '9']
input_a = [7,10,13,9,9,15,12,9,7,9]
input_b = [5,10,10,8,14,11,6,11,16,9]

X_axis = np.arange(len(X))

# csfont = {'fontname':'Comic Sans MS'}
# hfont = {'fontname':'Helvetica'}

# plt.title('title',**csfont)
# plt.xlabel('xlabel', **hfont)
# plt.show()
  
plt.bar(X_axis - 0.2, input_a, 0.4, label = r'$input_a$', zorder=3, color='#737373')
plt.bar(X_axis + 0.2, input_b, 0.4, label = r'$input_b$', zorder=3, color = '#93003a')
  
plt.xticks(X_axis, X)
plt.xlabel("Input values")
plt.ylabel("Count")
# plt.title("Number of Students in each group")
plt.legend()
plt.grid(axis = 'y', linestyle = '--', zorder=0)

plt.show()

