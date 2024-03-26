import numpy as np
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
from plot_utils import *
config['legend_prop_size'] = 42
config['xlabel'] = 'Token'
config['ylabel'] = 'Success Rate (\%)'
my_cmap = mpl.colormaps['tab20']
mpl.rcParams['text.usetex'] = True
plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')

# rafa step4 vicuna13B
plt.title(r'BlocksWorld (4-step), $\texttt{Vicuna-13B}$ ', size=40)
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
n_word = [38249, 57457, 76703, 96059, 115482, 154467, 193544, 232662, 291339, 369575, 506542, 584922, 722087, 839657, 1016012, 1113987, 1153177]
token_x = [50999, 76610, 102271, 128079, 153976, 205956, 258059, 310216, 388452, 492767, 675390, 779896, 962783, 1119543, 1354683, 1485316, 1537570]
success_rate_y = [22.8, 30.99, 36.4, 42.8, 48.2, 57.89, 64.9, 70.175, 75.43, 79.87, 84.5, 86.6, 89.14, 90.65687, 92.27, 92.95, 93.19]
ax.plot(token_x, success_rate_y, color=color_list[0], linewidth=10, label=r'\texttt{RAFA}')
'''---------'''
n_word = [38163, 57276, 76424, 95649, 114934, 153756, 173250, 192752, 212268, 231798, 251328, 368508, 583448, 818036, 994139, 1150859]
token_x = [50884, 76368, 101899, 127532, 153246, 205008, 231000, 257003, 283024, 309064, 335104, 491344, 777931, 1090715, 1325519, 1534479]
success_rate_y = [12.28, 15.78, 19.29, 24.21, 28.65, 39.47, 44.44, 48.77, 52.47, 55.70, 58.43, 68.79, 77.77, 82.62, 85.07, 86.97]
ax.plot(token_x, success_rate_y, color=color_list[1], linewidth=10, label=r'\texttt{RAP}')
# ax.plot([1], [48.77], color=color_list[1], linestyle='dashed', linewidth=10, marker='d', markersize=9, label=r'$\texttt{RAP(trial=10)}$')
# ax.plot([1], [68.79], color=color_list[2], linestyle='dashed', linewidth=10, marker='d', markersize=9, label=r'$\texttt{RAP(trial=20)}$')
# ax.axhline(y=48.77, color=color_list[1], linewidth=10, linestyle='-.', alpha=0.9)
# ax.axhline(y=68.79, color=color_list[2], linewidth=10, linestyle='-.', alpha=0.9)
'''---------'''
plt.xscale('log')
plt.ylim(-2, 100)
legend()
plt.tight_layout()
plt.savefig('step4_13b_token.pdf', format="pdf")