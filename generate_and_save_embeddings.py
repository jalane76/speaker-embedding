import click
import numpy as np
import os
from pathlib import Path
from speakerembeddings import SpeakerEmbeddings

@click.command()
@click.argument('data_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path())
@click.argument('model_path', type=click.Path(exists=True))
@click.option('--model_step', help='Ratio of audio chunk duration used as step between two consecutive audio chunks.')
def generate_and_save(data_path, output_path, model_path, model_step):

    files = sorted(os.listdir(data_path))
    print(f'Processing {len(files)} files from {data_path}...')

    ids = [f.split('.')[0] for f in files]
    model = SpeakerEmbeddings(model_path)

    embeddings, remove_indices = model.get_average_embeddings([os.path.join(data_path, f) for f in files], show_progress=True)
    for index in sorted(remove_indices, reverse=True):
        del ids[index]

    embeddings_dict = dict(zip(ids, embeddings))

    Path(output_path).mkdir(parents=True, exist_ok=True)
    with open(os.path.join(output_path, 'embeddings.npy'), 'wb') as out_file:
        # TODO: Need a better output format, this is a kludge
        np.save(out_file, embeddings_dict)


if __name__ == '__main__':
    generate_and_save()