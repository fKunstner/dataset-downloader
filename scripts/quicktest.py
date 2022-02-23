import dsdl
import pdb


datasets = ["concrete", "energy", "naval-propulsion", "power-plant"]

for dsname in datasets:
    ds = dsdl.load(dsname)
    print(dsname, ds)
