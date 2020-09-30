#/bin/bash

python generate_and_save_embeddings.py \
    /data/cmumosi/Raw/Audio/WAV_16000/Segmented/ \
    /data/speaker-embeddings/cmumosi/finetuned/ \
    /workspace/cmumosi-training-database/train/CMUMOSI.SpeakerDiarization.CMUMOSI.train/validate_diarization_fscore/CMUMOSI.SpeakerDiarization.CMUMOSI.development/