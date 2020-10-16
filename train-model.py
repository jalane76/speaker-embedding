#!/usr/bin/env python3

import click
from datetime import date, datetime
import logging
import os
from pathlib import Path
import shutil
import subprocess

def get_experiment_path(source_path, dest_path):
    # Get the leaf of the source_path
    base_name = os.path.basename(os.path.normpath(source_path))

    # Get an 8 digit date
    today = f'{date.today().year}{date.today().month:02}{date.today().day:02}'

    dated_name = '_'.join([base_name, today])

    # Find all the files generated today
    todays_files = [f for f in os.listdir(dest_path) if dated_name in f]

    # Get the increment of the file, e.g., '_3' for the 3rd file
    file_increments = [int(f[f.rfind('_') + 1:]) for f in todays_files]

    # Set the new file increment
    file_increment = 0
    if file_increments:
        file_increment = max(file_increments) + 1

    return os.path.join(dest_path, f'{dated_name}_{file_increment}')

def copy_files(source_path, dest_path):
    source_files = os.listdir(source_path)
    for file_name in source_files:
        file_path = os.path.join(source_path, file_name)
        if os.path.isfile(file_path):
            shutil.copy(file_path, dest_path)

@click.command()
@click.argument('train_db_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path())
@click.argument('protocol', type=str)
@click.option('--model_path', default=None, help='Path to the model weights')
@click.option('--epochs', default=10, help='Number of epochs to train')
def train(train_db_path, output_path, protocol, model_path, epochs):

    # Make sure output path exists
    Path(output_path).mkdir(parents=True, exist_ok=True)

    # Create unique experiment path
    experiment_path = get_experiment_path(train_db_path, output_path)
    Path(experiment_path).mkdir(parents=True, exist_ok=True)

    # Set up logging
    logging.basicConfig(
        filename=os.path.join(experiment_path, 'train.log'),
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s]:%(message)s'
    )

    # Copy all of the config and training files to the experiment directory
    copy_files(train_db_path, experiment_path)
    logging.info(f'Copied training files from {train_db_path} to {experiment_path}')

    # Build up the command line for the subprocess
    commands = ['pyannote-audio', 'emb', 'train', '--gpu']
    if model_path:
        model_file_name = os.path.basename(os.path.normpath(model_path))
        new_model_path = os.path.join(experiment_path, 'pyannote', 'needs', 'this')  # Dumb, but pyannote assumes the config is 3 dirs up from the model <sigh>
        Path(new_model_path).mkdir(parents=True, exist_ok=True)
        shutil.copy(model_path, new_model_path)
        new_model_path = os.path.join(new_model_path, model_file_name)
        commands.extend(['--pretrain', new_model_path])
    commands.extend([f'--to={epochs}', experiment_path, protocol])

    logging.info(f'Training command line: {" ".join(commands)}')

    cwd = os.getcwd()
    os.chdir(experiment_path)
    logging.info(f'Changed working directory {cwd} --> {experiment_path}')

    start_time = datetime.now()
    subprocess.run(commands)
    end_time = datetime.now()

    wall_time = end_time - start_time
    logging.info(f'Training took {wall_time}')

    os.chdir(cwd)
    logging.info(f'Changed working directory {experiment_path} --> {cwd}')

if __name__ == '__main__':
    train()