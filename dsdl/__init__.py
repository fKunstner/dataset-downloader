from dsdl.config import Config
from dsdl.dataset import is_downloaded, load
from dsdl.datasets_configs import DSETS


def available_datasets():
    return list(DSETS.keys())


def loader(dsname):
    return lambda: load(dsname)
