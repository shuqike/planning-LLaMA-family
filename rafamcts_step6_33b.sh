# id: 
# cuda-pid: 
for rollouts in 60
do
    CUDA_VISIBLE_DEVICES=7,8,9 nohup python -m torch.distributed.run --master_port 36977 --nproc_per_node 1 run_rafa_mcts.py --model_name Vicuna --verbose False --data data/blocksworld/step_6.json --max_depth 6 --name rafm_step6_33b_try${rollouts} --rollouts $rollouts --model_path lmsys/vicuna-33b-v1.3 --num_gpus 3 --resume_file_idx 8
done