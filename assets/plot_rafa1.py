import numpy as np
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
from plot_utils import *
config['xlabel'] = 'Steps'
config['ylabel'] = 'Success Rate (%)'
my_cmap = mpl.colormaps['tab20']
plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')

# rafa step4 vicuna13B
plt.title('Blocksworld Step4 Vicuna-13B', size=30)
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(16, 10)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
plt.tick_params('x', labelsize=20.0)
plt.tick_params('y', labelsize=20.0)
plt.xlabel(config['xlabel'], {'size': 26.0})
plt.ylabel(config['ylabel'], {'size': 26.0})
ax.xaxis.set_major_locator(ticker.MaxNLocator(6))
ax.yaxis.set_major_locator(ticker.MaxNLocator(6))
'''---------'''
sample_x = [2, 3, 4, 5, 6, 8, 10, 12, 15, 19, 26, 30, 37, 43, 52, 57, 59]
success_rate_y = [22.8, 30.99, 36.4, 42.8, 48.2, 57.89, 64.9, 70.175, 75.43, 79.87, 84.5, 86.6, 89.14, 90.65687, 92.27, 92.95, 93.19]
ax.plot(sample_x, success_rate_y, color=color_list[0], linewidth=3, label='RAFA')
'''---------'''
# sample_x = [59, 57, 52, 43, 37, 30, 26, 19, 15, 12, 10, 8, 6, 5, 4, 3, 2]
# success_rate_y = [86.9759, 86.5, 85.3, 82.9, 80.986, 77.77, 75.3, 68.79, 62.8, 55.7, 48.77, 39.47, 28.65, 24.21, 19.298, 15.789, 12.28]
# plt.plot(sample_x, success_rate_y, color=my_cmap(8), marker='o', markersize=9, linestyle='dashed', label='MCTS')
ax.plot([1], [48.77], color=color_list[1], marker='d', markersize=9, label=r'$\text{RAP}^{(10)}$')
ax.plot([1], [68.79], color=color_list[2], marker='d', markersize=9, label=r'$\text{RAP}^{(20)}$')
ax.axhline(y=48.77, color=color_list[1], linewidth=3, linestyle='-.', alpha=0.9)
ax.axhline(y=68.79, color=color_list[2], linewidth=3, linestyle='-.', alpha=0.9)
'''---------'''
plt.ylim(-2, 100)
legend()
plt.savefig('step4_13b.pdf', format="pdf")