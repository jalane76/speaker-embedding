#!/usr/bin/env python3

import click
import datetime
import logging
import multiprocessing
import os
from pathlib import Path
import subprocess
from tqdm import tqdm

def worker(command):
    subprocess.run(command, capture_output=False, shell=False, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

@click.command()
@click.argument('input_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path())
def extract(input_path, output_path):

    start_time = datetime.now()

    Path(output_path).mkdir(parents=True, exist_ok=True)

    # Set up logging
    logging.basicConfig(
        filename=os.path.join(output_path, 'audio.log'),
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s]:%(message)s'
    )

    in_files = os.listdir(input_path)
    logging.info(f'Processing {len(in_files)} audio files from {input_path}')
    logging.info(f'Saving to {output_path}')

    commands = []
    for in_file in tqdm(in_files):
        out_file = in_file.replace('.mp4', '.wav')
        in_path = os.path.join(input_path, in_file)
        out_path = os.path.join(output_path, out_file)

        ffmpeg_command = ['ffmpeg',
            '-i',
            in_path,
            '-b',
            '256K',
            '-ac',
            '1',
            '-ar',
            '16000',
            '-vn',
            out_path
        ]

        commands.append(ffmpeg_command)

    cpu_count = multiprocessing.cpu_count()
    logging.info(f'Processing with {cpu_count} workers...')
    with multiprocessing.Pool(processes=cpu_count) as pool:
        results = list(tqdm(pool.imap(worker, commands), total=len(in_files)))
    
    end_time = datetime.now()

    logging.info(f'Audio extraction took: {end_time - start_time}')

if __name__ == '__main__':
    extract()