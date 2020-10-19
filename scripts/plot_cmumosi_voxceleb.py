#!/usr/bin/env python3

import subprocess

def plot():
    script = '/workspace/plot-embeddings.py'
    data_path = '/data/speaker-embeddings/cmumosi/voxceleb/embeddings.npy'
    output_path = '/workspace/images/'
    title = 'CMU-MOSI VoxCeleb - Images'
    split_token = '_'
    annotation = 'image'
    num_annotations = '20'
    images_path = '/data/cmumosi/Raw/Image/Segmented'
    zoom = '0.2'
    
    commands = [
        script,
        data_path,
        output_path,
        title,
        '--split_token', split_token,
        '--annotation', annotation,
        '--num_annotations', num_annotations,
        '--images_path', images_path,
        '--zoom', zoom
    ]

    subprocess.run(commands)

if __name__ == '__main__':
    plot()