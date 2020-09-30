#/bin/bash

python plot-embeddings.py \
    /data/speaker-embeddings/cmumosi/finetuned/embeddings.npy \
    images/ \
    "CMU-MOSI Finetuned-ID" \
    --split_token="_" \
    --annotation="id" \
    --num_annotations=20