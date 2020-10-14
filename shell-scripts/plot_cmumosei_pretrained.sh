#/bin/bash

python /workspace/plot-embeddings.py \
    /data/speaker-embeddings/cmumosei/pretrained/embeddings.npy \
    /workspace/images/ \
    "CMU-MOSEI Pretrained-ID" \
    --annotation="id" \
    --num_annotations=20