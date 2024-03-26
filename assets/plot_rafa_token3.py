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


# rafa step6 vicuna 13B
plt.title(r'BlocksWorld (6-step), $\texttt{Vicuna-13B}$', size=40)
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
n_word = [53057, 159351, 212767, 319881, 427224, 534711, 696094, 857746, 1073540, 1235641, 1452072, 1723316, 1940662, 2267026, 2593576, 2974796, 3247178]
token_x = [70743, 212468, 283690, 426508, 569632, 712948, 928126, 1143662, 1431387, 1647522, 1936096, 2297755, 2587550, 3022702, 3458102, 3966395, 4329571]
success_rate_y = [0, 3.8, 7, 12.865, 18.53, 23.3, 28.87989, 34, 40, 43.8, 48, 53, 56.676, 61, 64.6, 68, 70]
ax.plot(token_x, success_rate_y, color=color_list[0], linewidth=10, label=r'\texttt{RAFA}')
'''---------'''
# sample_x = [1]
# success_rate_y = [40]
# ax.plot(sample_x, success_rate_y, color=color_list[1], linestyle='dashed', linewidth=10, label=r'\texttt{CoT(gpt-4)}')
# ax.axhline(y=40, color=color_list[1], linewidth=10, linestyle='-.', alpha=0.9)
# '''---------'''
n_word = [106137, 159174, 319073, 426112, 533235, 640557, 1070344, 1932054, 2687401, 3228530]
token_x = [141516, 212232, 425431, 568150, 710980, 854076, 1427126, 2576072, 3583202, 4304707]
success_rate_y = [0, 0, 3, 5.59, 8.07, 10.81, 19.47, 32.06, 39.19, 43.84]
plt.plot(token_x, success_rate_y, color=color_list[1], linewidth=10, label=r'\texttt{RAP}')
# ax.plot([1], [8], color=color_list[2], linestyle='dashed', linewidth=10, label=r'$\texttt{RAP(trial=10)}$')
# ax.axhline(y=8, color=color_list[2], linewidth=10, linestyle='-.', alpha=0.9)
# ax.plot([1], [19.47], color=color_list[3], linestyle='dashed', linewidth=10, label=r'$\texttt{RAP(trial=20)}$')
# ax.axhline(y=19.47, color=color_list[3], linewidth=10, linestyle='-.', alpha=0.9)
# '''---------'''
# sample_x = [1]
# success_rate_y = [0]
# ax.plot(sample_x, success_rate_y, color=color_list[4], linestyle='dashed', linewidth=10, label=r'\texttt{CoT(LLaMA-33B)}')
# ax.axhline(y=0, color=color_list[4], linewidth=10, linestyle='-.', alpha=0.9)
'''---------'''
plt.xscale('log')
plt.ylim(-2, 100)
legend()
plt.tight_layout()
plt.savefig('step6_13b_token.pdf', format='pdf')