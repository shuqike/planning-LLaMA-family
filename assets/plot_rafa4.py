import numpy as np
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
from plot_utils import *
config['legend_prop_size'] = 42
config['xlabel'] = 'Step'
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
sample_x = [1, 3, 4, 6, 8, 10, 13, 16, 20, 23, 27, 32, 36, 42, 48, 55, 60]
success_rate_y = [14, 23.9766, 27.85, 33.33, 37.28, 40.877, 45.7, 49.89, 54, 56.598, 59.55, 62.7, 64.9, 67.75, 70.23, 72.8, 74.4]
ax.plot(sample_x, success_rate_y, color=color_list[0], linewidth=10, label=r'\texttt{RAFA}')
'''---------'''
sample_x = [1]
success_rate_y = [40]
ax.plot(sample_x, success_rate_y, color=color_list[1], linestyle='dashed', linewidth=10, label=r'\texttt{CoT(gpt-4)}')
ax.axhline(y=40, color=color_list[1], linewidth=10, linestyle='-.', alpha=0.9)
'''---------'''
sample_x = [1]
success_rate_y = [0]
ax.plot(sample_x, success_rate_y, color=color_list[2], linestyle='dashed', linewidth=10, label=r'\texttt{CoT(LLaMA-33B)}')
ax.axhline(y=0, color=color_list[2], linewidth=10, linestyle='-.', alpha=0.9)
'''---------'''
plt.ylim(-2, 100)
legend()
plt.tight_layout()
plt.savefig('step6_33b.pdf', format='pdf')