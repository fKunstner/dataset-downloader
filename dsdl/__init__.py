from .datasets import load, is_downloaded
from . import config


def available_datasets():
    return list(config.DSETS.keys())


def loader(dsname):
    return lambda: load(dsname)
