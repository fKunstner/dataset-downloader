from .dataset import load, is_downloaded
from . import available_datasets
from .config import Config


def available_datasets():
    return list(available_datasets.DSETS.keys())


def loader(dsname):
    return lambda: load(dsname)
