import os
from . import config
import sklearn as sk
import sklearn.datasets
from .downloader import download_and_extract


class Dataset():
    def __init__(self, X_tr, y_tr, X_val=None, y_val=None, X_te=None, y_te=None, task=config.TASK_CLASS):
        assert task in config.AVAILABLE_TASKS
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
            return ("" if x[0] is None else str(x[0].shape)) + ("" if x[1] is None else ", " + str(x[1].shape))
        return str({
            "train": get_shape_or_none(self.get_train()),
            "val": get_shape_or_none(self.get_val()),
            "test": get_shape_or_none(self.get_test())
        })


def load_libsvm(dname):
    dsinfo = config.DSETS[dname]
    folder_path = os.path.join(config.DATA_ROOT, dname)

    path_tr = os.path.join(folder_path, dsinfo["train"])
    path_val = os.path.join(folder_path, dsinfo["val"]) if "val" in dsinfo else None
    path_te = os.path.join(folder_path, dsinfo["test"]) if "test" in dsinfo else None

    if not os.path.isfile(path_tr):
        for url in dsinfo["urls"]:
            download_and_extract(url, folder_path)

    tr = sk.datasets.load_svmlight_file(path_tr)
    val = sk.datasets.load_svmlight_file(path_val) if path_val is not None else (None, None)
    te = sk.datasets.load_svmlight_file(path_te) if path_te is not None else (None, None)
    return tr[0], tr[1], val[0], val[1], te[0], te[1]


def load(dname):
    return Dataset(*load_libsvm(dname), config.DSETS[dname]["TASK"])
