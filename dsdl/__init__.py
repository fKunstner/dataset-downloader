from .datasets import load
from . import config


def available_datasets():
    return list(config.DSETS.keys())


def small_datasets():
    for dsname in config.DSETS.keys():
        if config.DSETS[dsname].get("size", config.SIZE_SMALL) is config.SIZE_SMALL:
            yield dsname


def loader(dsname):
    return lambda: load(dsname)


def download_all_and_print_table():
    fstr = "| {task: <15} | {dsname: <120} | {tr: <22} | {val: <22} | {te: <22} |"

    def get_shape_or_none(x):
        return ("" if x[0] is None else str(x[0].shape)) + ("" if x[1] is None else ", " + str(x[1].shape))

    print(fstr.format(task="Task", dsname="Dataset", tr="Train (X, y)", val="Val (X, y)", te="Test (X, y)"))
    print(fstr.format(task="-", dsname="-", tr="-", val="-", te="-"))
    for dsname in small_datasets():
        ds = load(dsname)
        dsinfo = config.DSETS[dsname]
        print(fstr.format(
            task=ds.task,
            dsname="[" + dsname + "](" + dsinfo["url"] + ")",
            tr=get_shape_or_none(ds.get_train()),
            val=get_shape_or_none(ds.get_val()),
            te=get_shape_or_none(ds.get_test()),
        ))
