import numpy as np
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
from plot_utils import *
config['legend_prop_size'] = 42
config['xlabel'] = 'Token'
config['ylabel'] = 'Success Rate (\%)'
plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')


# rafa step6 vicuna 33B
plt.title(r'BlocksWorld (6-step), $\texttt{Vicuna-33B}$', size=40)
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(16, 10.8)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
plt.tick_params('x', labelsize=40.0)
plt.tick_params('y', labelsize=40.0)
plt.xlabel(config['xlabel'], {'size': 40.0})
plt.ylabel(config['ylabel'], {'size': 40.0})
ax.xaxis.set_major_locator(ticker.MaxNLocator(6))
ax.yaxis.set_major_locator(ticker.MaxNLocator(6))
'''---------'''
n_word = [108237, 270372, 541071, 1083950, 1628085, 2173043, 2718153, 3263280]
token_x = [144316, 360496, 721428, 1445267, 2170780, 2897391, 3624204, 4351040]
success_rate_y = [19.73, 30.70, 40.87, 54.12, 61.54, 66.88, 71.01, 74.4]
ax.plot(token_x, success_rate_y, color=color_list[0], linewidth=10, label=r'\texttt{RAFA}')
'''---------'''
n_word = [69987, 175074, 350034, 701096, 1053484, 1406038, 1758756, 2111767]
token_x = [93316, 233432, 466712, 934795, 1404646, 1874718, 2345008, 2815690]
success_rate_y = [4.6, 10.13, 15.86, 27.93, 35.82, 42.13, 47.84, 52.46]
ax.plot(token_x, success_rate_y, color=color_list[1], linewidth=10, label=r'\texttt{RAP}')
'''---------'''
plt.xscale('log')
plt.ylim(-2, 100)
legend()
plt.tight_layout()
plt.savefig('step6_33b_token.pdf', format='pdf')