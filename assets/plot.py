import matplotlib as mpl
import matplotlib.pyplot as plt
my_cmap = mpl.colormaps['tab20']

# for blocksworld step4 vicuna33B
# sample_x = [228, 444, 868, 1586, 11444, 14250, 17100]
# success_rate_y = [21.0526315789473, 40.3508771929824, 49.1228070175438, 61.4035087719298, 100, 100, 100]
# plt.plot(sample_x, success_rate_y, color='b', label='Our method')
# sample_x = [17100, 14250, 10260, 5700, 3420, 3135, 2850, 2280, 1995, 1710, 1425, 1140, 855, 570]
# success_rate_y = [100,98.25,96.49,89.47,85.96,82.46,80.70,80.70,77.19,75.44,68.42,57.89,52.63,26.32]
# plt.plot(sample_x, success_rate_y, color='r', label='MCTS')
# plt.ylabel('Success rate (%)')
# plt.xlabel('Sample')
# plt.title('Blocksworld Step4 Vicuna-33B')
# plt.legend()
# plt.show()

# for blocksworld step4 vicuna13B rulegoal
sample_x = [232, 856,1446,3288,11444,14250,17100]
success_rate_y = [93,100,100,100,100,100,100]
plt.plot(sample_x, success_rate_y, color='y', marker='o', markersize=9, linestyle='dashed', label='Rule-based subgoal setting')
sample_x = [232, 1434]
success_rate_y = [43.86, 73.68]
plt.plot(sample_x, success_rate_y, color='b', marker='o', markersize=9, linestyle='dashed', label='LLM-based subgoal setting')
# sample_x = [228,439,856,1446,3288,11444,14250,17100]
# success_rate_y = [12.28,15.79,36.84,47.37,64.91,100,100,100]
# plt.plot(sample_x, success_rate_y, color='b', label='Rough subgoal setting')
sample_x = [17100,14250,11400,10260,7980,5700,3705,3420,3135,2850,2565,2280,1995,1710,1425,1140,855,570,285]
success_rate_y = [100,98,94.74,94.74,92.98,92.98,91.23,91.23,89.47,87.72,84.21,77.19,66.67,50.88,43.86,29.82,22.81,12.28,12.28]
plt.plot(sample_x, success_rate_y, color='r', marker='o', markersize=9, linestyle='dashed', label='MCTS')
plt.ylabel('Success rate (%)')
plt.xlabel('Sample')
plt.title('Blocksworld Step4 Vicuna-13B')
plt.legend()
plt.show()

# for blocksworld step6 vicuna13B rulegoal
# plt.title('Blocksworld Step6 Vicuna-13B')
# sample_x = [728, 4621, 10591]
# success_rate_y = [61.4, 79.8, 99.1]
# plt.plot(sample_x, success_rate_y, color=my_cmap(8), marker='o', markersize=9, linestyle='dashed', label='Our method')
# sample_x = [1596, 2394, 3990, 4788, 5586, 6384, 7182, 7980, 8778, 9576, 15960, 28728, 39900, 47880] # treat multiple trials like one-shot
# success_rate_y = [0,  0, 6.1, 7.9, 10.5, 15.7, 16.6, 19.3, 22.8, 26.3, 37.7, 53.5, 61.4, 71.9] # treat multiple trials like one-shot
# plt.plot(sample_x, success_rate_y, color=my_cmap(4), marker='o', markersize=9, linestyle='dashed', label='MCTS')
# plt.ylabel('Success rate (%)')
# plt.xlabel('Sample')
# plt.legend()
# plt.show()