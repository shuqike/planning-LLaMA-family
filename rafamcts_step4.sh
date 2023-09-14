# id: 
CUDA_VISIBLE_DEVICES=6,7,8 nohup python -m torch.distributed.run --master_port 57271 --nproc_per_node 1 run_rafa_mcts.py \
--model_name Vicuna \
--name rafamcts_step4_13b \
--data data/blocksworld/step_4.json \
--n_trials 2 \
--horizon 4 \
--alpha 0.1 \
--model_path lmsys/vicuna-13b-v1.3 \
--num_gpus 3 \
--use_lang_goal