import os
import json
import argparse


def true_clip(x):
    return 1 if x else 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--run_name', type=str, default='mcts-run_1_Aug2_search_depth_3_alpha_01_rollouts_10')
    parser.add_argument('--num_trial', type=int, default=0)
    args = parser.parse_args()
    # if args.use_sample:
    data_path = os.path.join('logs', args.run_name, 'sample')
    sample_files = os.listdir(data_path)
    total_success = 0
    for file_name in sample_files:
        with open(os.path.join(data_path, file_name), 'r') as f:
            line = f.readline()
            try:
                num_success, num_sample = line.split(',')
            except:
                num_success = line.strip()
            if args.num_trial:
                total_success += eval(num_success)
            else:
                total_success += true_clip(eval(num_success))
    if args.num_trial:
        print(total_success/len(sample_files)/args.num_trial)
    else:
        print(total_success/len(sample_files))

    # sample accounting
    if not args.num_trial:
        data_path = os.path.join('logs', args.run_name, 'sample')
        sample_files = os.listdir(data_path)
        total_sample = 0
        total_success = 0
        for file_name in sample_files:
            with open(os.path.join(data_path, file_name), 'r') as f:
                line = f.readline()
                num_success, num_sample = line.split(',')
                try:
                    total_success += int(num_success)
                except ValueError:
                    total_success += bool(num_success)
                total_sample += int(num_sample)
        print(total_success, total_sample)
