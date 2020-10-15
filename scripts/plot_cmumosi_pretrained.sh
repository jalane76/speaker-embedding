#!/bin/bash

python /workspace/plot-embeddings.py \
    /data/speaker-embeddings/cmumosi/pretrained/embeddings.npy \
    /workspace/images/ \
    "CMU-MOSI Pretrained-ID" \
    --split_token="_" \
    --annotation="id" \
    --num_annotations=20