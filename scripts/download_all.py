import dsdl

for ds in dsdl.available_datasets():
    print(ds)
    if not dsdl.is_downloaded(ds):
        out = dsdl.load(ds)
