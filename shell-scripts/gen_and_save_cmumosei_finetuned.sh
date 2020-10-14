#/bin/bash

python /workspace/generate_and_save_embeddings.py \
    /data/cmumosei/Raw/Audio/Full/WAV_16000 \
    /data/speaker-embeddings/cmumosei/finetuned/ \
    /workspace/cmumosi-training-database/train/CMUMOSI.SpeakerDiarization.CMUMOSI.train/validate_diarization_fscore/CMUMOSI.SpeakerDiarization.CMUMOSI.development/