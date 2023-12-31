# id: 954028
CUDA_VISIBLE_DEVICES=0,1,2 nohup python -m torch.distributed.run --master_port 29400 --nproc_per_node 1 run_planning.py \
--model_name Vicuna \
--name planning_step6_13b_par \
--data data/blocksworld/step_6.json \
--horizon 6 \
--search_depth 3 \
--alpha 0 \
--sample_per_node 0 \
--model_path lmsys/vicuna-13b-v1.3 \
--num_gpus 3 \
--use_lang_goal