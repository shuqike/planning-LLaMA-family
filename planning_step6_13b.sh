# id: 
CUDA_VISIBLE_DEVICES=3,4,5 nohup python -m torch.distributed.run --master_port 1034 --nproc_per_node 1 run_planning.py \
--model_name Vicuna \
--name planning_step6_13b \
--data data/blocksworld/step_6.json \
--horizon 6 \
--search_depth 3 \
--alpha 0 \
--sample_per_node 2 \
--model_path lmsys/vicuna-13b-v1.3 \
--num_gpus 3 \
--use_lang_goal