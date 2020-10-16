#!/usr/bin/env python3

import subprocess

def validate():

    script = '/workspace/validate-model.py'
    training_db_path = '/data/speaker-embeddings/training/cmumosi-training-database_20201015_2'  #Add date and increment here
    protocol = 'CMUMOSI.SpeakerDiarization.CMUMOSI'
    to = '10'
    every = '1'

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