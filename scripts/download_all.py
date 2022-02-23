import dsdl

for ds in dsdl.available_datasets():
    print(ds)
    if dsdl.DSETS[ds]["format"] is "skl" or not dsdl.is_downloaded(ds):
        out = dsdl.load(ds)
