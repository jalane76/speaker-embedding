#/bin/bash

python plot-embeddings.py \
    /data/speaker-embeddings/cmumosei/pretrained/embeddings.npy \
    images/ \
    "CMU-MOSEI Pretrained-ID" \
    --annotation="id" \
    --num_annotations=20