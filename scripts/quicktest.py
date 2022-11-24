import pdb

import dsdl

datasets = ["movielens-100k", "movielens-1m"]

for dsname in datasets:
    ds = dsdl.load(dsname)
    print(dsname, ds)
