# id: 1453336
# cuda id: 1453403
CUDA_VISIBLE_DEVICES=0,1,2 nohup python -m torch.distributed.run --master_port 57271 --nproc_per_node 1 run_rafa.py \
--model_name Vicuna \
--name rafa_step6_33b \
--data data/blocksworld/step_6.json \
--n_trials 59 \
--horizon 6 \
--search_depth 2 \
--alpha 0 \
--sample_per_node 2 \
--model_path lmsys/vicuna-33b-v1.3 \
--num_gpus 3 \
--use_lang_goal \
--use_mem_prompt \
--resume_file_idx 35