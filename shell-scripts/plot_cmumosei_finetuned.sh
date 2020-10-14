#/bin/bash

python /workspace/plot-embeddings.py \
    /data/speaker-embeddings/cmumosei/finetuned/embeddings.npy \
    /workspace/images/ \
    "CMU-MOSEI Finetuned-ID" \
    --annotation="id" \
    --num_annotations=20