import numpy as np
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
from plot_utils import *
config['xlabel'] = 'Steps'
config['ylabel'] = 'Success Rate (%)'
plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')


# rafa step6 vicuna 13B
plt.title('Blocksworld Step6 Vicuna-13B', size=30)
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
sample_x = [1, 3, 4, 6, 8, 10, 13, 16, 20, 23, 27, 32, 36, 42, 48, 55, 60]
success_rate_y = [0, 3.8, 7, 12.865, 18.53, 23.3, 28.87989, 34, 40, 43.8, 48, 53, 56.676, 61, 64.6, 68, 70]
ax.plot(sample_x, success_rate_y, color=color_list[0], linewidth=3, label='RAFA')
'''---------'''
sample_x = [1]
success_rate_y = [40]
ax.plot(sample_x, success_rate_y, color=color_list[1], linewidth=3, label='CoT(gpt-4)')
ax.axhline(y=40, color=color_list[1], linewidth=3, linestyle='-.', alpha=0.9)
'''---------'''
# sample_x = [1, 3, 4, 6, 8, 10, 13, 16, 20, 23, 27, 32, 36, 42, 48, 55, 60]
# success_rate_y = [0, 0, 1, 3, 5.59, 8, 12, 15.296, 19.47, 22.27, 25.666, 29.44, 32, 35.359, 38.3, 41, 43.845]
# plt.plot(sample_x, success_rate_y, color=my_cmap(8), marker='o', markersize=9, linestyle='dashed', label='MCTS')
ax.plot([1], [8], color=color_list[2], linewidth=3, label=r'$\texttt{RAP}^{(10)}$')
ax.axhline(y=8, color=color_list[2], linewidth=3, linestyle='-.', alpha=0.9)
ax.plot([1], [19.47], color=color_list[3], linewidth=3, label=r'$\texttt{RAP}^{(20)}$')
ax.axhline(y=19.47, color=color_list[3], linewidth=3, linestyle='-.', alpha=0.9)
'''---------'''
sample_x = [1]
success_rate_y = [0]
ax.plot(sample_x, success_rate_y, color=color_list[4], linewidth=3, label='CoT(LLaMA-33B)')
ax.axhline(y=0, color=color_list[4], linewidth=3, linestyle='-.', alpha=0.9)
'''---------'''
plt.ylim(-2, 100)
legend()
plt.savefig('step6_13b.pdf', format='pdf')