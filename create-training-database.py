#!/usr/bin/env python3

import click
import contextlib
import os
from pathlib import Path
import random
from tqdm import tqdm
import wave

def strip_extension(s):
    return s[:s.rfind('.')]

def strip_file_increment(s):
    return s[:s.rfind('_')]

def write_list_file(file_path, file_list):
    with open(file_path, 'w') as out_file:
        uris = [strip_extension(f) for f in file_list]
        out_file.write('\n'.join(uris))

def write_reference_file(file_path, file_list, data_path):
    with open(file_path, 'w') as out_file:
        for file_name in tqdm(file_list):
            uri = strip_extension(file_name)
            speaker = strip_file_increment(uri)
            start = 0.0
            duration = 0.0
            with contextlib.closing(wave.open(os.path.join(data_path, file_name), 'r')) as wav_file:
                frames = wav_file.getnframes()
                rate = wav_file.getframerate()
                duration = frames / float(rate)
            out_file.write(f'SPEAKER {uri} 1 {start} {duration} <NA> <NA> {speaker} <NA> <NA>\n')

@click.command()
@click.argument('data_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path())
@click.option('--train_size', default=0.8, help='Value between 0.0 and 1.0 representing the portion of the data for training')
@click.option('--seed', default=12345, help='Seed for random number generation')
def create(data_path, output_path, train_size, seed):

    Path(output_path).mkdir(parents=True, exist_ok=True)
    files = os.listdir(data_path)

    random.seed(seed)
    random.shuffle(files)

    # Create training and test sets
    train_size = int(train_size * len(files))
    train_set = files[:train_size]
    test_set = files[train_size:]

    # Create training files
    write_list_file(os.path.join(output_path, 'train.lst'), train_set)
    write_reference_file(os.path.join(output_path, 'train.rttm'), train_set, data_path)
    
    # Create test files
    write_list_file(os.path.join(output_path, 'test.lst'), test_set)
    write_reference_file(os.path.join(output_path, 'test.rttm'), test_set, data_path)

if __name__ == '__main__':
    create()