#!/usr/bin/env python3

import subprocess

def train():

    script = '/workspace/train-model.py'
    training_db_path = '/workspace/cmumosi-training-database'
    output_path = '/data/speaker-embeddings/training/'
    protocol = 'CMUMOSI.SpeakerDiarization.CMUMOSI'
    model_path = '/data/speaker-embeddings/models/voxceleb-pretrained/0560.pt'

    subprocess.run([script, training_db_path, output_path, protocol, '--model_path', model_path, '--epochs', '3'])

if __name__ == '__main__':
    train()