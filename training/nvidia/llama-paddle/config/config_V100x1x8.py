split = "949,50,1"
max_seq_length = 2048
per_device_train_batch_size = 1
per_device_eval_batch_size = 1
use_flash_attention = 0
use_fused_rms_norm = 0 
fp16 = True
fp16_opt_level = 'O2'
gradient_accumulation_steps = 1
max_steps = 1000
eval_steps = 1000
learning_rate = 0.0001
min_learning_rate = 0.00001
weight_decay = 0.01
warmup_ratio = 0.01
log_freq = 20
seed = 42
sharding = "stage2"
use_recompute = True