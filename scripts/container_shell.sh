#!/bin/bash

singularity shell --nv \
    --bind /home/jalane/git/speaker-embedding:/workspace \
    --bind /data/Jesse:/data \
    /data/Jesse/singularity-images/speaker-embeddings_latest.sif