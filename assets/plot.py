import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from plot_utils import *

config['ylim'] = (0., 100.)
config['xlim'] = (0., 60)
config['xlabel'] = 'Steps'
config['ylabel'] = 'Success Rate (%)'
config['smooth_range'] = 1

legends = ['RAFA', r'$\texttt{RAP}^{(10)}$', r'$\texttt{RAP}^{(20)}$']

rafay = [22.8, 30.99, 36.4, 42.8, 48.2, 57.89, 64.9, 70.175, 75.43, 79.87, 84.5, 86.6, 89.14, 90.65687, 92.27, 92.95, 93.19]

datas = [
    [[2, 3, 4, 5, 6, 8, 10, 12, 15, 19, 26, 30, 37, 43, 52, 57, 59], rafay, np.zeros(len(rafay))],
    [[1], [48.77], np.zeros(len(rafay))],
    [[1], [68.79], np.zeros(len(rafay))],
]

plot_all(datas, legends, 1)

plt.title(f'Blocksworld', size=30)
legend()
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(16, 10)
plt.savefig(f"./rafa_step4_13b.pdf", format="pdf")
plt.show()
