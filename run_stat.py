import os
import json
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--run_name', type=str, default='mcts-run_1_Aug2_search_depth_3_alpha_01_rollouts_10')
    parser.add_argument('--use_sample', action='store_true')
    args = parser.parse_args()
    if args.use_sample:
        data_path = os.path.join('logs', args.run_name, 'sample')
        sample_files = os.listdir(data_path)
        total_success = 0
        for file_name in sample_files:
            with open(os.path.join(data_path, file_name), 'r') as f:
                line = f.readline()
                num_success, num_sample = line.split(',')
                total_success += eval(num_success)
    else:
        data_path = os.path.join('logs', args.run_name, 'json')
        sample_files = os.listdir(data_path)
        total_success = 0
        task_status = []
        for i, file_name in enumerate(sample_files):
            with open(os.path.join(data_path, file_name), 'r') as f:
                data = json.load(f)
                total_success += int(data[-1]['correct'])
                task_status.append([i, file_name, data[-1]['correct']])
        print(task_status)
    print(total_success/len(sample_files))
