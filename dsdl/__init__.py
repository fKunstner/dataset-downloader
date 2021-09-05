from .dataset import load, is_downloaded
from .available_datasets import DSETS
from .config import Config


def available_datasets():
    return list(DSETS.keys())


def loader(dsname):
    return lambda: load(dsname)
