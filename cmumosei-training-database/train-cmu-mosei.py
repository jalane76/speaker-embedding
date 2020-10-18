#!/usr/bin/env python3

import subprocess

def train():

    script = '/workspace/train-model.py'
    training_db_path = '/workspace/cmumosei-training-database'
    output_path = '/data/speaker-embeddings/training/'
    protocol = 'CMUMOSEI.SpeakerDiarization.CMUMOSEI'
    #model_path = '/data/speaker-embeddings/models/voxceleb-pretrained/0560.pt'

    commands = [
        script,
        training_db_path,
        output_path,
        protocol,
        #'--model_path', model_path,
        '--epochs', '1000'
    ]

    subprocess.run(commands)

if __name__ == '__main__':
    train()