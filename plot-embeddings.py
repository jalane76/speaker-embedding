#!/usr/bin/env python3

import click
import logging
from matplotlib import pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
import os
from pathlib import Path
from scipy.spatial.distance import cdist
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

@click.command()
@click.argument('embeddings_file_path', type=click.File('rb'))
@click.argument('output_path', type=click.Path())
@click.argument('title')
@click.option('--seed', default=12345, help='Seed for random number generation')
@click.option('--split_token', default='', help='Token to split identifiers')  # TODO: more elegant solution (regular expressions?)
@click.option('--annotation', type=click.Choice(['None', 'ID', 'Image'], case_sensitive=False), help='The type of annotations to add to the plot')
@click.option('--num_annotations', default=0, help='The number of annotations to add to the plot')
@click.option('--images_path', default=None, type=click.Path(exists=True), help='Path to the images')
@click.option('--zoom', default=0.2, help='Zoom level for annotation images')
def plot(embeddings_file_path, output_path, title, seed, split_token, annotation, num_annotations, images_path, zoom):

    # Load embeddings TODO: less kludgey data format
    Path(output_path).mkdir(parents=True, exist_ok=True)

    # Set up logging
    logging.basicConfig(
        filename=os.path.join(output_path, 'plot.log'),
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s]:%(message)s'
    )

    logging.info(f'Loading embeddings from {embeddings_file_path}')
    embeddings_dict = np.load(embeddings_file_path, allow_pickle=True)

    # Separate the ids and embeddings
    ids = list(embeddings_dict.item().keys())
    embeddings = [embeddings_dict[()][id] for id in ids]
    embeddings = np.vstack(embeddings)

    # Remove segmented file indices and get unique ids
    if split_token != '':
        ids = [id[:id.rfind(split_token)] for id in ids]
    _, unique_ids = np.unique(ids, return_inverse=True)
    
    # Get t-SNE embeddings
    logging.info('Generating t-SNE...')
    tsne_embeddings = TSNE(n_components=2, metric='cosine', random_state=seed).fit_transform(embeddings)
    logging.debug(f't-SNE embedding shape: {tsne_embeddings.shape}')

    # Get PCA embeddings
    logging.info('Generating PCA...')
    pca_embeddings = PCA(n_components=2, random_state=seed).fit_transform(embeddings)
    logging.debug(f'PCA embedding shape: {pca_embeddings.shape}')

    logging.info('Plotting...')

    fig, axes = plt.subplots(1, 2)
    fig.set_figheight(10)
    fig.set_figwidth(20)
    fig.suptitle(title)

    axes[0].scatter(*tsne_embeddings.T, c=unique_ids, cmap=plt.cm.Spectral, s=1)
    axes[0].set_title('t-SNE')

    annotation = annotation.lower()
    if annotation != 'none' and num_annotations > 0:
        step_size = int(len(ids) / num_annotations)
        for i in range(0, len(ids), step_size):
            id = ids[i]
            if annotation == 'id':
                axes[0].annotate(id, (tsne_embeddings[i, 0], tsne_embeddings[i, 1]))
                axes[1].annotate(id, (pca_embeddings[i, 0], pca_embeddings[i, 1]))
            elif annotation == 'image' and images_path:
                image_dir = [f for f in os.listdir(images_path) if id in f][0]
                image_file = os.listdir(os.path.join(images_path, image_dir))[0]
                im_path = os.path.join(images_path, image_dir, image_file)
                image = OffsetImage(plt.imread(im_path), zoom=zoom)

                # t-SNE
                x, y = tsne_embeddings[i,:]
                ab = AnnotationBbox(image, (x, y), frameon=False)
                axes[0].add_artist(ab)

                # PCA
                x, y = pca_embeddings[i,:]
                ab = AnnotationBbox(image, (x, y), frameon=False)
                axes[1].add_artist(ab)


    axes[1].scatter(*pca_embeddings.T, c=unique_ids, cmap=plt.cm.Spectral, s=1)
    axes[1].set_title('PCA')

    title_no_spaces = title.replace(' ', '_')
    filename = f'{title_no_spaces}.png'
    plt.savefig(os.path.join(output_path, filename), dpi=500)


if __name__ == '__main__':
    plot()