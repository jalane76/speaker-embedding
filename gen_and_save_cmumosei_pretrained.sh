#/bin/bash

python generate_and_save_embeddings.py \
    /data/cmumosei/Raw/Audio/Full/WAV_16000 \
    /data/speaker-embeddings/cmumosei/pretrained/ \
    /repos/SpeakerEmbeddingLossComparison/models/AAM/train/VoxCeleb.SpeakerVerification.VoxCeleb2.train/validate_equal_error_rate/VoxCeleb.SpeakerVerification.VoxCeleb1_X.development/