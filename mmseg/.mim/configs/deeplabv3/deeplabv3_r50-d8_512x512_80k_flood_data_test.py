_base_ = [
    '../_base_/models/deeplabv3_r50-d8.py',
    '../_base_/datasets/flood.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_40k.py'
]
model = dict(
    pretrained = None,
    backbone=dict(in_channels=2),
    decode_head=dict(num_classes=2),
    auxiliary_head=dict(num_classes=2),
    test_cfg=dict(mode='slide', crop_size=(480, 480), stride=(320, 320)))

test_pipeline = [
    dict(type='LoadImageFromFile_flood'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(512, 512),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect_flood_test', keys=['img']),
        ])
]
data = dict(
    test=dict(
        pipeline=test_pipeline))
optimizer = dict(type='SGD', lr=0.004, momentum=0.9, weight_decay=0.0001)
evaluation = dict(interval=4000, metric='mIoU')
