# id: 
CUDA_VISIBLE_DEVICES=7,8,9 nohup python -m torch.distributed.run --master_port 1034 --nproc_per_node 1 run_planning.py \
--model_name Vicuna \
--name planning_step4_13b \
--data data/blocksworld/step_4.json \
--horizon 4 \
--search_depth 2 \
--alpha 0 \
--sample_per_node 2 \
--model_path lmsys/vicuna-13b-v1.3 \
--num_gpus 3