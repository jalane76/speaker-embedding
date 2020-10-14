#/bin/bash

python /workspace/plot-embeddings.py \
    /data/speaker-embeddings/cmumosi/finetuned/embeddings.npy \
    /workspace/images/ \
    "CMU-MOSI Finetuned-ID" \
    --split_token="_" \
    --annotation="id" \
    --num_annotations=20