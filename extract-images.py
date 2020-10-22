#!/usr/bin/env python3

import click
from datetime import datetime
import logging
import os
from pathlib import Path
import subprocess
from tqdm import tqdm

@click.command()
@click.argument('input_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path())
@click.option('--width', default=224, help='Output image width in pixels')
@click.option('--height', default=224, help='Output image height in pixels')
@click.option('--scale', default=1.0, help='Output image will be scaled by scale * width and scale * height')
def extract(input_path, output_path, width, height, scale):
    start_time = datetime.now()

    Path(output_path).mkdir(parents=True, exist_ok=True)

    # Set up logging
    logging.basicConfig(
        filename=os.path.join(output_path, 'images.log'),
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s]:%(message)s'
    )

    in_files = os.listdir(input_path)
    logging.info(f'Processing {len(in_files)} videos from {input_path}')
    logging.info(f'Saving to {output_path}')

    image_size = (int(scale * width), int(scale * height))
    logging.info(f'Output image size: {image_size}')

    for in_file in tqdm(in_files):
        in_path = os.path.join(input_path, in_file)
        logging.debug(f'In path {in_path}')

        out_path = os.path.join(output_path, in_file[:in_file.rfind('.')])
        logging.debug(f'Out path {out_path}')

        Path(out_path).mkdir(parents=True, exist_ok=True)

        ffmpeg_command = [
            'ffmpeg',
            '-i',
            in_path,
            '-vf', f'scale={image_size[0]}:{image_size[1]}:force_original_aspect_ratio=decrease,pad={image_size[0]}:{image_size[1]}:-1:-1:color=black',
            os.path.join(out_path, 'img%06d.png')
        ]
        logging.debug(f'ffmpeg command: {" ".join(ffmpeg_command)}')
        subprocess.run(
            ffmpeg_command,
            capture_output=False,
            shell=False,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    
    end_time = datetime.now()
    logging.info(f'Image extraction took: {end_time - start_time}')
        

if __name__ == '__main__':
    extract()