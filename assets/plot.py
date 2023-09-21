import numpy as np
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
plt.plot(sample_x, success_rate_y, color='y', marker='o', markersize=9, linestyle='dashed', label='[Domain]Rule-based subgoal')
'''---------'''
sample_x = [232, 683, 1434, 3187, 3402, 11832]
success_rate_y = [43.86, 43.86, 73.68, 80.7, 84.21, 100]
plt.plot(sample_x, success_rate_y, color='b', marker='o', markersize=9, linestyle='dashed', label='[Domain]LLM-based subgoal')
'''---------'''
sample_x = [228,439,856,1446,3288,11444,14250,17100]
success_rate_y = [12.28,15.79,36.84,47.37,64.91,100,100,100]
plt.plot(sample_x, success_rate_y, color='purple', marker='o', markersize=9, linestyle='dashed', label='[Rough]Rule-based subgoal')
'''---------'''
sample_x = [16815, 16245, 14820, 12255, 10545, 8550, 7410, 5415, 4275, 3420, 2850, 2280, 1425, 1140, 855, 570]
success_rate_y = [86.9759, 86.5, 85.3, 82.9, 80.986, 77.77, 75.3, 68.79, 62.8, 55.7, 48.77, 39.47, 24.21, 19.298, 15.789, 12.28]
plt.plot(sample_x, success_rate_y, color='r', marker='o', markersize=9, linestyle='dashed', label='MCTS')
'''---------'''
plt.ylabel('Success rate (%)')
plt.xlabel('Sample')
plt.title('Blocksworld Step4 Vicuna-13B')
plt.legend()
plt.show()

# for blocksworld step6 vicuna13B rulegoal
plt.title('Blocksworld Step6 Vicuna-13B')
sample_x = [728, 4621, 10591]
success_rate_y = [61.4, 79.8, 99.1]
plt.plot(sample_x, success_rate_y, color=my_cmap(8), marker='o', markersize=9, linestyle='dashed', label='[Domain]Rule-based subgoal')
'''partial notes
bad pl6_serd3_sampall(38518, 57.89)
good pl4_serd4_samp2(28739, 55.26)
'''
sample_x = [784, 5167, 13097, 28739]
success_rate_y = [12.28, 26.3, 42.98, 55.26]
plt.plot(sample_x, success_rate_y, color=my_cmap(12), marker='o', markersize=9, linestyle='dashed', label='[Domain]LLM-based subgoal')
sample_x = [1596, 2394, 3990, 4788, 5586, 6384, 7182, 7980, 8778, 9576, 15960, 28728, 39900, 47880] # treat multiple trials like one-shot
success_rate_y = [0,  0, 6.1, 7.9, 10.5, 15.7, 16.6, 19.3, 22.8, 26.3, 37.7, 53.5, 61.4, 71.9] # treat multiple trials like one-shot
plt.plot(sample_x, success_rate_y, color=my_cmap(4), marker='o', markersize=9, linestyle='dashed', label='MCTS')
plt.ylabel('Success rate (%)')
plt.xlabel('Sample')
plt.legend()
plt.show()

# rafa step4 vicuna13B
plt.title('Blocksworld Step4 Vicuna-13B')
'''---------'''
sample_x = [2, 3, 4, 5, 6, 8, 10, 12, 15, 19, 26, 30, 37, 43, 52, 57, 59]
success_rate_y = [22.8, 30.99, 36.4, 42.8, 48.2, 57.89, 64.9, 70.175, 75.43, 79.87, 84.5, 86.6, 89.14, 90.65687, 92.27, 92.95, 93.19]
# success_rate_y = np.array(success_rate_y) - 22.8 + 12.28
plt.plot(sample_x, success_rate_y, color=my_cmap(12), marker='o', markersize=9, linestyle='dashed', label='RAFA')
'''---------'''
sample_x = [59, 57, 52, 43, 37, 30, 26, 19, 15, 12, 10, 8, 6, 5, 4, 3, 2]
success_rate_y = [86.9759, 86.5, 85.3, 82.9, 80.986, 77.77, 75.3, 68.79, 62.8, 55.7, 48.77, 39.47, 28.65, 24.21, 19.298, 15.789, 12.28]
plt.plot(sample_x, success_rate_y, color=my_cmap(8), marker='o', markersize=9, linestyle='dashed', label='MCTS')
# '''---------'''
# sample_x = [2, 3]
# success_rate_y = [71.9, 71.9]
# plt.plot(sample_x, success_rate_y, color=my_cmap(4), marker='o', markersize=9, linestyle='dashed', label='MPC-bfs(b=2)')
plt.ylim(-2, 100)
plt.ylabel('Success Rate (%)')
plt.xlabel('Episode')
plt.legend(loc='lower right')
plt.show()

# rafa step4 vicuna33B
plt.title('Blocksworld Step4 Vicuna-33B')
'''---------'''
sample_x = [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 19, 26, 30, 37, 43, 52, 57, 59]
success_rate_y = [43.8596, 53.5, 62.57, 68.42, 72.98, 76.3, 80.7, 83.5, 85.38, 87.6, 89.658, 91.97, 92.8, 94.12, 94.94, 95.8, 96.18, 96.3128]
plt.plot(sample_x, success_rate_y, color=my_cmap(12), marker='o', markersize=9, linestyle='dashed', label='RAFA')
'''---------'''
sample_x = [1]
success_rate_y = [63]
plt.plot(sample_x, success_rate_y, color=my_cmap(4), marker='d', markersize=9, linestyle='dashed', label='CoT(gpt-4)')
'''---------'''
sample_x = [1]
success_rate_y = [2]
plt.plot(sample_x, success_rate_y, color=my_cmap(2), marker='d', markersize=9, linestyle='dashed', label='CoT')
'''---------'''
sample_x = [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 19, 26, 30, 37, 43, 52, 57, 59]
success_rate_y = [21, 23.68, 33.33, 39.47, 45.26, 50.29, 57.456, 62.1, 65.789, 69.94, 73.96, 78.6, 80.526, 83.357, 85.4, 87.7, 88.79655, 89.17633]
plt.plot(sample_x, success_rate_y, color=my_cmap(8), marker='o', markersize=9, linestyle='dashed', label='MCTS')
'''---------'''
plt.axvline(x=1, color='black', linestyle='-.', alpha=0.2)
plt.axhline(y=2, color='black', linestyle='-.', alpha=0.2)
plt.axhline(y=63, color='black', linestyle='-.', alpha=0.2)
'''---------'''
plt.ylim(-2, 100)
plt.ylabel('Success Rate (%)')
plt.xlabel('Episode')
plt.legend(loc='lower right')
plt.show()

# rafa step6 vicuna 13B
plt.title('Blocksworld Step6 Vicuna-13B')
'''---------'''
sample_x = [1, 3, 4, 6, 8, 10, 13, 16, 20, 23, 27, 32, 36, 42, 48, 55, 60]
success_rate_y = [0, 3.8, 7, 12.865, 18.53, 23.3, 28.87989, 34, 40, 43.8, 48, 53, 56.676, 61, 64.6, 68, 70]
plt.plot(sample_x, success_rate_y, color=my_cmap(12), marker='o', markersize=9, linestyle='dashed', label='RAFA')
'''---------'''
sample_x = [1]
success_rate_y = [40]
plt.plot(sample_x, success_rate_y, color=my_cmap(4), marker='d', markersize=9, linestyle='dashed', label='CoT(gpt-4)')
'''---------'''
sample_x = [1, 3, 4, 6, 8, 10, 13, 16, 20, 23, 27, 32, 36, 42, 48, 55, 60]
success_rate_y = [0, 0, 1, 3, 5.59, 8, 12, 15.296, 19.47, 22.27, 25.666, 29.44, 32, 35.359, 38.3, 41, 43.845]
plt.plot(sample_x, success_rate_y, color=my_cmap(8), marker='o', markersize=9, linestyle='dashed', label='MCTS')
'''---------'''
sample_x = [1]
success_rate_y = [0]
plt.plot(sample_x, success_rate_y, color=my_cmap(2), marker='d', markersize=9, linestyle='dashed', label='CoT')
'''---------'''
plt.axvline(x=1, color='black', linestyle='-.', alpha=0.2)
plt.axhline(y=40, color='black', linestyle='-.', alpha=0.2)
'''---------'''
plt.ylim(-2, 100)
plt.ylabel('Success Rate (%)')
plt.xlabel('Episode')
plt.legend(loc='lower right')
plt.show()