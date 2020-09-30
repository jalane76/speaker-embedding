#/bin/bash

python plot-embeddings.py \
    /data/speaker-embeddings/cmumosei/finetuned/embeddings.npy \
    images/ \
    "CMU-MOSEI Finetuned-ID" \
    --annotation="id" \
    --num_annotations=20