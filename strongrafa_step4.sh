# id: 
# cuda id: 
for rollouts in 60
do
    CUDA_VISIBLE_DEVICES=4,6,9 nohup python -m torch.distributed.run --master_port 39855 --nproc_per_node 1 run_srm.py --model_name Vicuna --verbose False --data data/blocksworld/step_4.json --max_depth 4 --name srm_step4_33b_try${rollouts} --rollouts $rollouts --model_path lmsys/vicuna-33b-v1.3 --num_gpus 3 --resume_file_idx 11
done