#!/usr/bin/env python3

import click
import logging
import numpy as np
import os
from pathlib import Path
from speakerembeddings import SpeakerEmbeddings

@click.command()
@click.argument('data_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path())
@click.argument('model_path', type=click.Path(exists=True))
def generate_and_save(data_path, output_path, model_path):

    Path(output_path).mkdir(parents=True, exist_ok=True)

    # Set up logging
    logging.basicConfig(
        filename=os.path.join(output_path, 'gen_and_save.log'),
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s]:%(message)s'
    )

    files = sorted(os.listdir(data_path))
    logging.info(f'Processing {len(files)} files from {data_path}...')

    ids = [f.split('.')[0] for f in files]

    logging.info(f'Loading model at {model_path}...')
    model = SpeakerEmbeddings(model_path)

    logging.info('Calculating embeddings...')
    embeddings, remove_indices = model.get_average_embeddings([os.path.join(data_path, f) for f in files], show_progress=True)

    logging.info('Removing failed or empty embeddings...')
    for index in sorted(remove_indices, reverse=True):
        del ids[index]

    embeddings_dict = dict(zip(ids, embeddings))

    logging.info(f'Saving embeddings in {output_path}')
    with open(os.path.join(output_path, 'embeddings.npy'), 'wb') as out_file:
        # TODO: Need a better output format, this is a kludge
        np.save(out_file, embeddings_dict)


if __name__ == '__main__':
    generate_and_save()