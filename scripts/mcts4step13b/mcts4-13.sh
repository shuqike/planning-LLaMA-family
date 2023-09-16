# id: 252203
for rollouts in 2 3 4 5 6 7 8 9 10 11 12 13
do
    CUDA_VISIBLE_DEVICES=8,9 nohup python -m torch.distributed.run --master_port 34471 --nproc_per_node 1 run_mcts.py --task mcts --model_name Vicuna --verbose False \
    --data data/blocksworld/step_4.json \
    --max_depth 4 \
    --name mcts4rest${rollouts} \
    --rollouts $rollouts \
    --model_path lmsys/vicuna-13b-v1.3 \
    --num_gpus 2
done