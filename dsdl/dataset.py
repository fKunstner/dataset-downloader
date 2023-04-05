import os

import numpy as np
import pandas as pd
import scipy as sp
import sklearn as sk
import sklearn.datasets
from scipy import sparse

from dsdl import datasets_configs
from dsdl.config import Config
from dsdl.downloader import download_and_extract


class Dataset:
    def __init__(
        self,
        X_tr,
        y_tr,
        X_val=None,
        y_val=None,
        X_te=None,
        y_te=None,
        task=datasets_configs.TASK_CLASS,
    ):
        assert task in datasets_configs.AVAILABLE_TASKS
        self.X_tr = X_tr
        self.y_tr = y_tr
        self.X_val = X_val
        self.y_val = y_val
        self.X_te = X_te
        self.y_te = y_te
        self.task = task

    def get_train(self):
        return self.X_tr, self.y_tr

    def get_val(self):
        return self.X_val, self.y_val

    def get_test(self):
        return self.X_te, self.y_te

    def __str__(self):
        def get_shape_or_none(x):
            return ("" if x[0] is None else str(x[0].shape)) + (
                "" if x[1] is None else ", " + str(x[1].shape)
            )

        return str(
            {
                "train": get_shape_or_none(self.get_train()),
                "val": get_shape_or_none(self.get_val()),
                "test": get_shape_or_none(self.get_test()),
            }
        )


def is_downloaded(dname):
    dsinfo = datasets_configs.DSETS[dname]
    folder_path = os.path.join(Config.get("DATA_ROOT"), dname)
    if "subfolder" in dsinfo:
        path_tr = os.path.join(folder_path, dsinfo["subfolder"], dsinfo["train"])
    else:
        path_tr = os.path.join(folder_path, dsinfo["train"])
    return os.path.isfile(path_tr)


def load_libsvm(dname, split=None):
    if split is not None:
        raise ValueError(f"Splits are not supported for dataset {dname}")
    dsinfo = datasets_configs.DSETS[dname]
    folder_path = os.path.join(Config.get("DATA_ROOT"), dname)

    path_tr = os.path.join(folder_path, dsinfo["train"])
    path_val = os.path.join(folder_path, dsinfo["val"]) if "val" in dsinfo else None
    path_te = os.path.join(folder_path, dsinfo["test"]) if "test" in dsinfo else None

    if not is_downloaded(dname):
        for url in dsinfo["urls"]:
            download_and_extract(url, folder_path)

    tr = sk.datasets.load_svmlight_file(path_tr)
    val = (
        sk.datasets.load_svmlight_file(path_val)
        if path_val is not None
        else (None, None)
    )
    te = (
        sk.datasets.load_svmlight_file(path_te) if path_te is not None else (None, None)
    )
    return tr[0], tr[1], val[0], val[1], te[0], te[1]


def load_skl(dname, split=None):
    if split is not None:
        raise ValueError(f"Splits are not supported for dataset {dname}")
    loader = getattr(sk.datasets, datasets_configs.DSETS[dname]["skl_loader"])
    x_tr, y_tr = loader(return_X_y=True)
    return x_tr, y_tr, None, None, None, None


def load_uci(dname, split=None):
    if split is not None:
        raise ValueError(f"Splits are not supported for dataset {dname}")
    dsinfo = datasets_configs.DSETS[dname]
    folder_path = os.path.join(Config.get("DATA_ROOT"), dname)

    if not is_downloaded(dname):
        for url in dsinfo["urls"]:
            download_and_extract(url, folder_path)

    def load_if_exist(data_subset):
        if data_subset not in dsinfo:
            return None, None
        path = os.path.join(folder_path, dsinfo[data_subset])
        if ".xls" in path:
            data = pd.read_excel(path).to_numpy()
        else:
            data = np.loadtxt(path)

        x = data[:, dsinfo["features"]] if "features" in dsinfo else data[:, :-1]
        y = data[:, dsinfo["target"]] if "target" in dsinfo else data[:, -1]

        return x, y

    x_tr, y_tr = load_if_exist("train")
    x_val, y_val = load_if_exist("val")
    x_te, y_te = load_if_exist("test")

    return x_tr, y_tr, x_val, y_val, x_te, y_te


def load_movielens_100k(dname, split=None):
    dsinfo = datasets_configs.DSETS[dname]
    folder_path = os.path.join(Config.get("DATA_ROOT"), dname)

    if not is_downloaded(dname):
        download_and_extract(dsinfo["url"], folder_path)

    def read(filepath):
        data = np.genfromtxt(filepath, usecols=(0, 1, 2))
        user_id = data[:, 0].astype(int)
        movie_id = data[:, 1].astype(int)
        ratings = data[:, 2]
        return sp.sparse.coo_matrix((ratings, (user_id, movie_id)))

    if split is None:
        path_tr = os.path.join(folder_path, dsinfo["subfolder"], dsinfo["train"])
        path_te = None
    elif split in [1, 2, 3, 4, 5]:
        path_tr = os.path.join(folder_path, dsinfo["subfolder"], f"u{split}.base")
        path_te = os.path.join(folder_path, dsinfo["subfolder"], f"u{split}.test")
    elif split in ["a", "b"]:
        path_tr = os.path.join(folder_path, dsinfo["subfolder"], f"u{split}.base")
        path_te = os.path.join(folder_path, dsinfo["subfolder"], f"u{split}.test")
    else:
        raise ValueError(
            f"Unknown split {split}. "
            f"Can be None to get the entire dataset as training,"
            f"in [1, 2, 3, 4, 5] for a 20/80 split, "
            f"or in ['a', 'b'] for a 10-item/user split."
        )

    X_tr = read(path_tr) if path_tr is not None else None
    X_te = read(path_te) if path_te is not None else None

    return X_tr, None, None, None, X_te, None


def load_movielens_1m(dname, split=None):
    if split is not None:
        raise ValueError(f"Splits are not supported for dataset {dname}")

    dsinfo = datasets_configs.DSETS[dname]
    folder_path = os.path.join(Config.get("DATA_ROOT"), dname)

    if not is_downloaded(dname):
        download_and_extract(dsinfo["url"], folder_path)

    path = os.path.join(folder_path, dsinfo["subfolder"], dsinfo["train"])
    data = np.genfromtxt(path, delimiter="::", usecols=(0, 1, 2))
    user_id = data[:, 0].astype(int)
    movie_id = data[:, 1].astype(int)
    ratings = data[:, 2]
    X = sp.sparse.coo_matrix((ratings, (user_id, movie_id)))
    return X, None, None, None, None, None


def load_faithful(dname, split=None):
    if split is not None:
        raise ValueError(f"Splits are not supported for dataset {dname}")

    dsinfo = datasets_configs.DSETS[dname]
    folder_path = os.path.join(Config.get("DATA_ROOT"), dname)

    if not is_downloaded(dname):
        download_and_extract(dsinfo["url"], folder_path)
    path = os.path.join(folder_path, dsinfo["train"])
    data = np.genfromtxt(path, skip_header=26, usecols=(1, 2))
    return data, None, None, None, None, None


def load_other(dname, split=None):

    if dname == "faithful":
        return load_faithful(dname)
    elif dname == "movielens-100k":
        return load_movielens_100k(dname, split)
    elif dname == "movielens-1m":
        return load_movielens_1m(dname, split)
    else:
        raise ValueError(f"Unknown dataset {dname}.")


def load(dname, split=None):
    dataset = datasets_configs.DSETS[dname]
    if dataset["format"] == "skl":
        return Dataset(*load_skl(dname, split), dataset["TASK"])
    elif dataset["format"] == "uci":
        return Dataset(*load_uci(dname, split), dataset["TASK"])
    elif dataset["format"] == "libsvm":
        return Dataset(*load_libsvm(dname, split), dataset["TASK"])
    elif dataset["format"] == "other":
        return Dataset(*load_other(dname, split), dataset["TASK"])
    else:
        raise ValueError(f"Unknown dataset format for {dname}: {dataset}")
