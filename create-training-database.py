import click
import contextlib
import os
from pathlib import Path
import random
import wave

@click.command()
@click.argument('data_path')
@click.argument('output_path')
@click.option('--seed', default=12345, help='Seed for random number generation')
def create(data_path, output_path, seed):

    Path(output_path).mkdir(parents=True, exist_ok=True)
    files = os.listdir(data_path)

    random.seed(seed)
    random.shuffle(files)

    # Create training and test sets TODO: add dev split option
    train_size = int(0.8 * len(files)) # TODO: remove hardcoded split
    train_set = files[:train_size]
    test_set = files[train_size:]

    # Create training files
    with open(os.path.join(output_path, 'train.lst'), 'w') as train_list_file:
        uris = [f.split('.')[0] for f in train_set]
        train_list_file.write('\n'.join(uris))

    with open(os.path.join(output_path, 'train.rttm'), 'w') as train_rttm_file:
        for file_name in train_set:
            uri = file_name.split('.')[0]
            speaker = uri.split('_')[0]
            start = 0.0
            duration = 0.0
            with contextlib.closing(wave.open(os.path.join(data_path, file_name), 'r')) as wav_file:
                frames = wav_file.getnframes()
                rate = wav_file.getframerate()
                duration = frames / float(rate)
            train_rttm_file.write(f'SPEAKER {uri} 1 {start} {duration} <NA> <NA> {speaker} <NA> <NA>\n')


    # Create test files
    with open(os.path.join(output_path, 'test.lst'), 'w') as test_list_file:
        uris = [f.split('.')[0] for f in test_set]
        test_list_file.write('\n'.join(uris))

    with open(os.path.join(output_path, 'test.rttm'), 'w') as test_rttm_file:
        for file_name in test_set:
            uri = file_name.split('.')[0]
            speaker = uri.split('_')[0]
            start = 0.0
            duration = 0.0
            with contextlib.closing(wave.open(os.path.join(data_path, file_name), 'r')) as wav_file:
                frames = wav_file.getnframes()
                rate = wav_file.getframerate()
                duration = frames / float(rate)
            test_rttm_file.write(f'SPEAKER {uri} 1 {start} {duration} <NA> <NA> {speaker} <NA> <NA>\n')

if __name__ == '__main__':
    create()