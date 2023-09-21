import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--num_trial', type=int, default=0)
args = parser.parse_args()
num_trial = args.num_trial


succ = 0
for i in range(114):
    f = open("./json/" + "{:04d}".format(i) + ".json")
    data = json.load(f)
    for j in range(num_trial):
        succ += int(data[j]["correct"])
print(succ / 114 / num_trial)