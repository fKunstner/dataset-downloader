# Dataset Downloader

Some utilities to download and load datasets to numpy arrays.
No preprocessing.

Install `pip install git+https://github.com/fkunstner/dataset-downloader.git`

Use `import dsdl`, `ds = dsdl.load("a1a")`, `X, y = ds.get_train()`, 

Requirements `scikit-learn`, `numpy`

# Datasets available

* [LIBSVM binary datasets](https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary.html)
* [LIBSVM regression datasets](https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/regression.html)
* Some datasets from Scikit-learn and UCI. [See full list](available_datasets.md).

# Usage

```
import dsdl

print(dsdl.available_datasets())

# > ['a1a', 'a2a', 'a3a', 'a4a', 'a5a', 'a6a', 'a7a', 'a8a', 'a9a', 'australian', 'australian_scale', 'breast-cancer', 'breast-cancer_scale', 'cod-rna', 'colon-cancer', 'covtype.binary', 'covtype.binary.scale', 'diabetes', 'diabetes_scale', 'duke-breast-cancer', 'fourclass', 'fourclass_scale', 'german.numer', 'german.numer_scale', 'gisette', 'heart', 'heart_scale', 'ijcnn1', 'ionosphere', 'leukemia', 'madelon', 'mushrooms', 'news20.binary', 'phishing', 'rcv1.binary', 'real-sim', 'skin_nonskin', 'splice', 'sonar', 'svmguide1', 'svmguide3', 'w1a', 'w2a', 'w3a', 'w4a', 'w5a', 'w6a', 'w7a', 'w8a', 'abalone', 'abalone_scale', 'bodyfat', 'bodyfat_scale', 'cadata', 'cpusmall', 'cpusmall_scale', 'E2006-log1p', 'E2006-E2006-tfidf', 'eunite2001', 'mg', 'mg_scale', 'mpg', 'mpg_scale', 'pyrim', 'pyrim_scale', 'space_ga', 'space_ga_scale', 'triazines', 'triazines_scale', 'YearPredictionMSD', 'yacht', 'boston-housing', 'california-housing', 'concrete', 'energy', 'naval-propulsion', 'power-plant', 'digits', 'faithful']
ds = dsdl.load("a1a")

X, y = ds.get_train()
print(X.shape, y.shape)
# > (1605, 119) (1605,)

X_te, y_te = ds.get_test()
print(X_te.shape, y_te.shape)
# > (30956, 123) (30956,)
```


