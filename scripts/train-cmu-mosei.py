#!/usr/bin/env python3

import subprocess

# NOTE: The pyannote training script excepts the config.yml file to be in the root of the model path
def train():

    script = '/workspace/train-model.py'
    training_db_path = '/workspace/cmumosei-training-database'
    output_path = '/data/speaker-embeddings/training/'
    protocol = 'CMUMOSEI.SpeakerDiarization.CMUMOSEI'
    model_path = '/data/speaker-embeddings/models/voxceleb-pretrained/0560.pt'

    subprocess.run([script, training_db_path, output_path, protocol, '--model_path', model_path])

if __name__ == '__main__':
    train()