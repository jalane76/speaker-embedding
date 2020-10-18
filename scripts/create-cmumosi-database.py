#!/usr/bin/env python3

import subprocess

def create():
    script = '/workspace/create-training-database.py'
    data_path = '/data/cmumosi/Raw/Audio/WAV_16000/Segmented/'
    output_path = '/workspace/cmumosi-training-database/'

    commands = [
        script,
        data_path,
        output_path
    ]

    subprocess.run(commands)

if __name__ == '__main__':
    create()