# id: 
for rollouts in 5 6 7 8 10 12 15 19 26 30 37 43 52 57 59
do
    CUDA_VISIBLE_DEVICES=6,7,8 nohup python -m torch.distributed.run --master_port 57271 --nproc_per_node 1 run_rafa_mcts.py --model_name Vicuna --verbose False --data data/blocksworld/step_4.json --max_depth 4 --name rafm_step4_13b_try${rollouts} --rollouts $rollouts --model_path lmsys/vicuna-13b-v1.3 --num_gpus 3
done