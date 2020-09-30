#/bin/bash

python plot-embeddings.py \
    /data/speaker-embeddings/cmumosi/pretrained/embeddings.npy \
    images/ \
    "CMU-MOSI Pretrained-ID" \
    --split_token="_" \
    --annotation="id" \
    --num_annotations=20