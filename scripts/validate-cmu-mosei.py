#!/usr/bin/env python3

import subprocess

def validate():

    script = '/workspace/validate-model.py'
    training_db_path = '/data/speaker-embeddings/training/cmumosei-training-database_20201015_4'  #Add date and increment here
    protocol = 'CMUMOSEI.SpeakerDiarization.CMUMOSEI'
    to = '1000'
    every = '5'

    commands = [
        script,
        training_db_path,
        protocol,
        '--to', to,
        '--every', every
    ]

    subprocess.run(commands)

if __name__ == '__main__':
    validate()