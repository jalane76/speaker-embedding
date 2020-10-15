#!/bin/bash

python /workspace/generate_and_save_embeddings.py \
    /data/cmumosi/Raw/Audio/WAV_16000/Segmented/ \
    /data/speaker-embeddings/cmumosi/pretrained/ \
    /repos/SpeakerEmbeddingLossComparison/models/AAM/train/VoxCeleb.SpeakerVerification.VoxCeleb2.train/validate_equal_error_rate/VoxCeleb.SpeakerVerification.VoxCeleb1_X.development/