CUDA_VISIBLE_DEVICES=0,1,2,3 python -m torch.distributed.launch --nproc_per_node=4 --master_port=9005 ./tools/train.py --launcher pytorch ./configs/deeplabv3/deeplabv3_r50-d8_512x512_80k_flood_data_aug.py
