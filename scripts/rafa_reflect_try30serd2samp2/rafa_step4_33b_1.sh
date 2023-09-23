# id: 1416851
# cuda id: 
CUDA_VISIBLE_DEVICES=0,1,2 nohup python -m torch.distributed.run --master_port 57271 --nproc_per_node 1 run_rafa.py \
--model_name Vicuna \
--name rafa_step4_13b \
--data data/blocksworld/step_4.json \
--n_trials 30 \
--horizon 4 \
--search_depth 2 \
--alpha 0 \
--sample_per_node 2 \
--model_path lmsys/vicuna-33b-v1.3 \
--num_gpus 3 \
--use_lang_goal \
--use_mem_prompt \
--resume_file_idx 13