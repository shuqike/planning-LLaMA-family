# id: 
# cuda id: 
for rollouts in 60
do
    CUDA_VISIBLE_DEVICES=6,7,8 nohup python -m torch.distributed.run --master_port 1034 --nproc_per_node 1 run_mcts.py --task mcts --model_name Vicuna --verbose False --data data/blocksworld/step_6.json --max_depth 6 --name m6ct_roll${rollouts} --rollouts $rollouts --model_path lmsys/vicuna-33b-v1.3 --num_gpus 3 --resume_file_idx 67
done