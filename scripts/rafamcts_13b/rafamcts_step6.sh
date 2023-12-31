# id: 1840008
# cuda-pid: 1840123
for rollouts in 60
do
    CUDA_VISIBLE_DEVICES=0,1,2 nohup python -m torch.distributed.run --master_port 57271 --nproc_per_node 1 run_rafa_mcts.py --model_name Vicuna --verbose False --data data/blocksworld/step_6.json --max_depth 6 --name rafm_step6_13b_try${rollouts} --rollouts $rollouts --model_path lmsys/vicuna-13b-v1.3 --num_gpus 3 --resume_file_idx 58
done