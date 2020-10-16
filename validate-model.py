#!/usr/bin/env python3

import click
from datetime import datetime
import logging
import os
from pathlib import Path
import subprocess

@click.command()
@click.argument('experiment_path', type=click.Path(exists=True))
@click.argument('protocol', type=str)
@click.option('--subset', default='test', help='Portion of the dataset to use for validation')
@click.option('--to', default='100', help='Epoch to stop validating')
@click.option('--every', default='5', help='Validate every <--every> epoch')
def validate(experiment_path, protocol, subset, to, every):

    # Create the training directory
    train_path = os.path.join(experiment_path, 'train', '.'.join([protocol, 'train']))
    Path(train_path).mkdir(parents=True, exist_ok=True)

    # Set up logging
    logging.basicConfig(
        filename=os.path.join(experiment_path, 'validate.log'),
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s]:%(message)s'
    )

    commands = [
        'pyannote-audio',
        'emb',
        'validate',
        '--subset', subset,
        '--to', to,
        '--every', every,
        train_path,
        protocol
    ]

    logging.info(f'Validating command line: {" ".join(commands)}')

    cwd = os.getcwd()
    os.chdir(experiment_path)
    logging.info(f'Changed working directory {cwd} --> {experiment_path}')

    start_time = datetime.now()
    subprocess.run(commands)
    end_time = datetime.now()

    wall_time = end_time - start_time
    logging.info(f'Validation took {wall_time}')

    os.chdir(cwd)
    logging.info(f'Changed working directory {experiment_path} --> {cwd}')

if __name__ == '__main__':
    validate()