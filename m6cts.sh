for rollouts in 60
do
    CUDA_VISIBLE_DEVICES=9,8,7 nohup python -m torch.distributed.run --master_port 1034 --nproc_per_node 1 run_blocksworld.py --task mcts --model_name Vicuna --verbose False --data data/blocksworld/step_6.json --max_depth 6 --name m6ct_roll${rollouts} --rollouts $rollouts --model_path lmsys/vicuna-33b-v1.3 --num_gpus 3
done