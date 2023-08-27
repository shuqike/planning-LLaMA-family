# id: 
CUDA_VISIBLE_DEVICES=0,1 nohup python -m torch.distributed.run --master_port 29400 --nproc_per_node 1 run_planning.py \
--model_name Vicuna \
--name planning_step4_7b \
--data data/blocksworld/step_4.json \
--horizon 4 \
--search_depth 2 \
--alpha 0 \
--sample_per_node 2 \
--model_path lmsys/vicuna-7b-v1.3 \
--num_gpus 2