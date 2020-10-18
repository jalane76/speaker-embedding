#!/usr/bin/env python3

import subprocess

def plot():
    script = '/workspace/plot-embeddings.py'
    data_path = '/data/speaker-embeddings/cmumosei/voxceleb/embeddings.npy'
    output_path = '/workspace/images/'
    title = 'CMU-MOSEI VoxCeleb'
    split_token = '_'
    annotation = 'none'
    num_annotations = '20'
    
    commands = [
        script,
        data_path,
        output_path,
        title,
        '--split_token', split_token,
        '--annotation', annotation,
        '--num_annotations', num_annotations
    ]

    subprocess.run(commands)

if __name__ == '__main__':
    plot()