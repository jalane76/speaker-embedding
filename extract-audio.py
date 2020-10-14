import click
import os
from pathlib import Path
import subprocess
from tqdm import tqdm

@click.command()
@click.argument('input_path')
@click.argument('output_path')
def extract(input_path, output_path):
    Path(output_path).mkdir(parents=True, exist_ok=True)
    in_files = os.listdir(input_path)

    for in_file in tqdm(in_files):
        out_file = in_file.replace('.mp4', '.wav')
        in_path = os.path.join(input_path, in_file)
        out_path = os.path.join(output_path, out_file)
        ffmpeg_command = ['ffmpeg', '-i', in_path, '-b', '256K', '-ac', '1', '-ar', '16000', '-vn', out_path]
        subprocess.run(ffmpeg_command, capture_output=False, shell=False, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if __name__ == '__main__':
    extract()