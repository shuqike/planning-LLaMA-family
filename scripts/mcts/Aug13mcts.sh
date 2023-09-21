for rollouts in 2 3 4 5 6 7 8 9 10 11 12 20 36 50 60
do
    CUDA_VISIBLE_DEVICES=0,1,2,3 nohup python -m torch.distributed.run --master_port 1034 --nproc_per_node 1 run_blocksworld.py --task mcts --model_name Vicuna --verbose False --data data/blocksworld/step_4.json --max_depth 4 --name Aug13mcts${rollouts} --rollouts $rollouts --model_path lmsys/vicuna-33b-v1.3 --num_gpus 4 > Aug13mcts${rollouts}.txt
done