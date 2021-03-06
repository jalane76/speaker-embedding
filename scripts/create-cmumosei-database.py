#!/usr/bin/env python3

import subprocess

def create():
    script = '/workspace/create-training-database.py'
    data_path = '/data/cmumosei/Raw/Audio/Segmented/Combined/WAV_16000/'
    output_path = '/workspace/cmumosei-training-database/'

    commands = [
        script,
        data_path,
        output_path
    ]

    subprocess.run(commands)

if __name__ == '__main__':
    create()