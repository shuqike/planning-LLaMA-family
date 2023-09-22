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


# rafa step4 vicuna33B
plt.title('Blocksworld Step4 Vicuna-33B', size=30)
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
# '''---------'''
# sample_x = [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 19, 26, 30, 37, 43, 52, 57, 59]
# success_rate_y = [50.877, 60.5, 67.8, 71.9, 74.7, 77, 80.9, 84, 86, 88.4, 90.674, 93, 94, 95.2, 95.879, 96.59, 96.89, 96.99]
# plt.plot(sample_x, success_rate_y, color=my_cmap(14), marker='o', markersize=9, linestyle='dashed', label='RAFA-n')
'''---------'''
sample_x = [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 19, 26, 30, 37, 43, 52, 57, 59]
success_rate_y = [43.8596, 53.5, 62.57, 68.42, 72.98, 76.3, 80.7, 83.5, 85.38, 87.6, 89.658, 91.97, 92.8, 94.12, 94.94, 95.8, 96.18, 96.3128]
ax.plot(sample_x, success_rate_y, color=color_list[0], linewidth=3, label='RAFA')
'''---------'''
sample_x = [1]
success_rate_y = [63]
ax.plot(sample_x, success_rate_y, color=color_list[1], marker='d', markersize=9, linestyle='dashed', label='CoT(gpt-4)')
ax.axhline(y=63, color=color_list[1], linestyle='-.', linewidth=3, alpha=0.2)
'''---------'''
sample_x = [1]
success_rate_y = [2]
ax.plot(sample_x, success_rate_y, color=color_list[2], marker='d', markersize=9, linestyle='dashed', label='CoT(LLaMA-33B)')
ax.axhline(y=2, color=color_list[2], linestyle='-.', linewidth=3, alpha=0.2)
'''---------'''
# sample_x = [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 19, 26, 30, 37, 43, 52, 57, 59]
# success_rate_y = [21, 23.68, 33.33, 39.47, 45.26, 50.29, 57.456, 62.1, 65.789, 69.94, 73.96, 78.6, 80.526, 83.357, 85.4, 87.7, 88.79655, 89.17633]
# plt.plot(sample_x, success_rate_y, color=my_cmap(8), marker='o', markersize=9, linestyle='dashed', label='MCTS')
ax.plot([1], [62.1], color=color_list[3], marker='d', markersize=9, label=r'$\texttt{RAP}^{(10)}$')
ax.axhline(y=62.1, color=color_list[3], linestyle='-.', linewidth=3, alpha=0.5)
ax.plot([1], [73.96], color=color_list[4], marker='d', markersize=9, label=r'$\texttt{RAP}^{(20)}$')
ax.axhline(y=73.96, color=color_list[4], linestyle='-.', linewidth=3, alpha=0.5)
'''---------'''
ax.axvline(x=1, color='black', linestyle='-.', linewidth=3, alpha=0.2)
'''---------'''
plt.ylim(-2, 100)
legend()
plt.savefig('step4_33b.pdf', format='pdf')