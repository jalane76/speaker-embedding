#!/usr/bin/env python3

import subprocess

def gen_and_save():
    script = '/workspace/generate_and_save_embeddings.py'
    data_path = '/data/cmumosi/Raw/Audio/WAV_16000/Segmented/'
    output_path = '/data/speaker-embeddings/cmumosi/retrained/'
    model_path = ('/data/speaker-embeddings/models/cmumosei_retrained/'
        'train/CMUMOSEI.SpeakerDiarization.CMUMOSEI.train/validate_equal_error_rate/'
        'VoxCeleb.SpeakerVerification.VoxCeleb1_X.development/'
    )
    
    commands = [
        script,
        data_path,
        output_path,
        model_path
    ]

    subprocess.run(commands)

if __name__ == '__main__':
    gen_and_save()    