import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--num_trial', type=int, default=0)
args = parser.parse_args()
num_trial = args.num_trial


succ = 0
for i in range(114):
    f = open("./sample/" + "{:04d}".format(i) + ".accn")
    data = f.readline()
    start_idx = int(data.split(',')[0])
    if start_idx != -1:
        succ += max(num_trial - start_idx, 0)
print(succ / 114 / num_trial)