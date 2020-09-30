import numpy as np
import os
from pathlib import Path
from pyannote.audio.features import Pretrained
import torch
from tqdm import tqdm

class SpeakerEmbeddings:

    def __init__(
        self,
        weights_path: Path = None,
        step: float = 0.0333
    ):

        try:
            weights_path = Path(weights_path)
        except TypeError as e:
            msg = (
                f'"weights_path" must be str, bytes, or os.PathLike object, not {type(weights_path).__name__}.'
            )
            raise TypeError(msg)
    
        self._model = Pretrained(weights_path, step=step)

    def get_average_embeddings(self, audio_files: list, show_progress: bool = False) -> np.ndarray:
        embeddings = []
        remove_indices = []
        if show_progress:
            audio_files = tqdm(audio_files)
        for i, f in enumerate(audio_files):
            try:
                emb = np.mean(self._model({'audio': f}), axis=0)
            except:  # TODO: be more elegant here
                emb = None
            if emb is None or emb.shape[0] != self._model.dimension:
                remove_indices.append(i)
            embeddings.append(emb)
        for index in sorted(remove_indices, reverse=True):
            del embeddings[index]
        embeddings = np.vstack(embeddings)
        return embeddings, remove_indices