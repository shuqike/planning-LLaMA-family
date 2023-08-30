# 
for rollouts in 2 3 4 5 6 7 8 9 10 11 12 20 36 50 60
do
    CUDA_VISIBLE_DEVICES=0,1,2 nohup python -m torch.distributed.run --master_port 1034 --nproc_per_node 1 run_mcts.py --task mcts --model_name Vicuna --verbose False --data data/blocksworld/step_6.json --max_depth 6 --name step6_13b_roll${rollouts} --rollouts $rollouts --model_path lmsys/vicuna-13b-v1.3 --num_gpus 3
done