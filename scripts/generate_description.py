"""Generate dataset description."""

import os
import dsdl
from pathlib import Path

fstr = "| {task: <14} | {format:<10} | {dsname: <130} | {tr: <26} | {val: <26} | {te: <26} | {tsize: <10} |"


def get_shape_or_none(x):
    return ("" if x[0] is None else str(x[0].shape)) + (
        "" if x[1] is None else ", " + str(x[1].shape)
    )


def total_size(dname):
    f_path = Path(os.path.join(dsdl.config.Config.get("DATA_ROOT"), dname))
    tot_bytes = sum(f.stat().st_size for f in f_path.glob("**/*") if f.is_file())

    def sizeof_fmt(num, suffix="B"):
        for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
            if abs(num) < 1024.0:
                return "%3.0f%s%s" % (num, unit, suffix)
            num /= 1024.0
        return "%.0f%s%s" % (num, "Yi", suffix)

    return sizeof_fmt(tot_bytes)


print("# Datasets")
print()
print(
    fstr.format(
        task="Task",
        format="Format",
        dsname="Dataset",
        tr="Train (X, y)",
        val="Validation (X, y)",
        te="Test (X, y)",
        tsize="Total size",
    )
)

print(fstr.format(task="-", format="-", dsname="-", tr="-", val="-", te="-", tsize="-"))

for dsname in dsdl.available_datasets():
    ds = dsdl.load(dsname)
    dsinfo = dsdl.DSETS[dsname]
    print(
        fstr.format(
            task=ds.task,
            format=dsinfo["format"],
            dsname="[{}]({})".format(dsname, dsinfo["url"]),
            tr=get_shape_or_none(ds.get_train()),
            val=get_shape_or_none(ds.get_val()),
            te=get_shape_or_none(ds.get_test()),
            tsize=total_size(dsname),
        )
    )
