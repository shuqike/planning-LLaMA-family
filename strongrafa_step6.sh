# id: 
# cuda id: 
for rollouts in 60
do
    CUDA_VISIBLE_DEVICES=1,2,6 nohup python -m torch.distributed.run --master_port 54543 --nproc_per_node 1 run_srm.py --model_name Vicuna --verbose False --data data/blocksworld/step_6.json --max_depth 6 --name srm_step6_33b_try${rollouts} --rollouts $rollouts --model_path lmsys/vicuna-33b-v1.3 --num_gpus 3
done