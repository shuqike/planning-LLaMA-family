# rafa step6 vicuna 13B
plt.clf()
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
# sample_x = [1, 3, 4, 6, 8, 10, 13, 16, 20, 23, 27, 32, 36, 42, 48, 55, 60]
# success_rate_y = [0, 0, 1, 3, 5.59, 8, 12, 15.296, 19.47, 22.27, 25.666, 29.44, 32, 35.359, 38.3, 41, 43.845]
# plt.plot(sample_x, success_rate_y, color=my_cmap(8), marker='o', markersize=9, linestyle='dashed', label='MCTS')
plt.plot([1], [8], color=my_cmap(7), marker='d', markersize=9, label=r'$\texttt{RAP}^{(10)}$')
plt.plot([1], [19.47], color=my_cmap(8), marker='d', markersize=9, label=r'$\texttt{RAP}^{(20)}$')
plt.axhline(y=8, color=my_cmap(7), linestyle='-.', alpha=0.5)
plt.axhline(y=19.47, color=my_cmap(8), linestyle='-.', alpha=0.5)
'''---------'''
sample_x = [1]
success_rate_y = [0]
plt.plot(sample_x, success_rate_y, color=my_cmap(2), marker='d', markersize=9, linestyle='dashed', label='CoT(LLaMA-33B)')
'''---------'''
plt.axvline(x=1, color='black', linestyle='-.', alpha=0.2)
plt.axhline(y=0, color='black', linestyle='-.', alpha=0.2)
plt.axhline(y=40, color='black', linestyle='-.', alpha=0.2)
'''---------'''
plt.ylim(-2, 100)
plt.ylabel('Success Rate (%)')
plt.xlabel('Episode')
plt.legend(loc='lower right')
plt.savefig('step6_13b.png', dpi=600)

# rafa step6 vicuna 33B
plt.clf()
plt.title('Blocksworld Step6 Vicuna-33B')
'''---------'''
sample_x = [1, 3, 4, 6, 8, 10, 13, 16, 20, 23, 27, 32, 36, 42, 48, 55, 60]
success_rate_y = [14, 23.9766, 27.85, 33.33, 37.28, 40.877, 45.7, 49.89, 54, 56.598, 59.55, 62.7, 64.9, 67.75, 70.23, 72.8, 74.4]
plt.plot(sample_x, success_rate_y, color=my_cmap(12), marker='o', markersize=9, linestyle='dashed', label='RAFA')
'''---------'''
sample_x = [1]
success_rate_y = [40]
plt.plot(sample_x, success_rate_y, color=my_cmap(4), marker='d', markersize=9, linestyle='dashed', label='CoT(gpt-4)')
'''---------'''
sample_x = [1]
success_rate_y = [0]
plt.plot(sample_x, success_rate_y, color=my_cmap(2), marker='d', markersize=9, linestyle='dashed', label='CoT(LLaMA-33B)')
'''---------'''
plt.axvline(x=1, color='black', linestyle='-.', alpha=0.2)
plt.axhline(y=0, color='black', linestyle='-.', alpha=0.2)
plt.axhline(y=40, color='black', linestyle='-.', alpha=0.2)
'''---------'''
plt.ylim(-2, 100)
plt.ylabel('Success Rate (%)')
plt.xlabel('Episode')
plt.legend(loc='lower right')
plt.savefig('step6_33b.png', dpi=600)