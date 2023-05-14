import os

TASK_CLASS = "Classification"
TASK_MULTICLASS = "Multiclass Classification"
TASK_REG = "Regression"
TASK_CLU = "Clustering"
TASK_REC = "Recommendation"

SIZE_SMALL = "small"
SIZE_MEDIUM = "medium"
SIZE_LARGE = "large"

AVAILABLE_TASKS = [TASK_CLASS, TASK_MULTICLASS, TASK_REG, TASK_CLU, TASK_REC]


def libsvm_url(category, file):
    return "https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/{}/{}".format(
        category, file
    )


def libsvm_ds_url(category, dsname):
    return "https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/{}.html#{}".format(
        category, dsname
    )


def uci_url(dsname):
    return "https://archive.ics.uci.edu/ml/datasets/{}".format(dsname)


def uci_ds_url(end):
    return "https://archive.ics.uci.edu/ml/machine-learning-databases/{}".format(end)


def skl_url(dsname):
    return "https://scikit-learn.org/stable/modules/generated/sklearn.datasets.{}.html".format(
        dsname
    )


def delve_url(s):
    return "https://www.cs.toronto.edu/~delve/data/{}".format(s)


def delve_ds_url(s):
    return "ftp://ftp.cs.toronto.edu/pub/neuron/delve/data/tarfiles/{}".format(s)


DSETS = {
    "a1a": {
        "url": libsvm_ds_url("binary", "a1a"),
        "urls": [libsvm_url("binary", "a1a"), libsvm_url("binary", "a1a.t")],
        "train": "a1a",
        "test": "a1a.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "a2a": {
        "url": libsvm_ds_url("binary", "a2a"),
        "urls": [libsvm_url("binary", "a2a"), libsvm_url("binary", "a2a.t")],
        "train": "a2a",
        "test": "a2a.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "a3a": {
        "url": libsvm_ds_url("binary", "a3a"),
        "urls": [libsvm_url("binary", "a3a"), libsvm_url("binary", "a3a.t")],
        "train": "a3a",
        "test": "a3a.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "a4a": {
        "url": libsvm_ds_url("binary", "a4a"),
        "urls": [libsvm_url("binary", "a4a"), libsvm_url("binary", "a4a.t")],
        "train": "a4a",
        "test": "a4a.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "a5a": {
        "url": libsvm_ds_url("binary", "a5a"),
        "urls": [libsvm_url("binary", "a5a"), libsvm_url("binary", "a5a.t")],
        "train": "a5a",
        "test": "a5a.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "a6a": {
        "url": libsvm_ds_url("binary", "a6a"),
        "urls": [libsvm_url("binary", "a6a"), libsvm_url("binary", "a6a.t")],
        "train": "a6a",
        "test": "a6a.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "a7a": {
        "url": libsvm_ds_url("binary", "a7a"),
        "urls": [libsvm_url("binary", "a7a"), libsvm_url("binary", "a7a.t")],
        "train": "a7a",
        "test": "a7a.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "a8a": {
        "url": libsvm_ds_url("binary", "a8a"),
        "urls": [libsvm_url("binary", "a8a"), libsvm_url("binary", "a8a.t")],
        "train": "a8a",
        "test": "a8a.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "a9a": {
        "url": libsvm_ds_url("binary", "a9a"),
        "urls": [libsvm_url("binary", "a9a"), libsvm_url("binary", "a9a.t")],
        "train": "a9a",
        "test": "a9a.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "australian": {
        "url": libsvm_ds_url("binary", "australian"),
        "urls": [libsvm_url("binary", "australian")],
        "train": "australian",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "australian_scale": {
        "url": libsvm_ds_url("binary", "australian"),
        "urls": [libsvm_url("binary", "australian_scale")],
        "train": "australian_scale",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "breast-cancer": {
        "url": libsvm_ds_url("binary", "breast-cancer"),
        "urls": [libsvm_url("binary", "breast-cancer")],
        "train": "breast-cancer",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "breast-cancer_scale": {
        "url": libsvm_ds_url("binary", "breast-cancer"),
        "urls": [libsvm_url("binary", "breast-cancer")],
        "train": "breast-cancer",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "cod-rna": {
        "url": libsvm_ds_url("binary", "cod-rna"),
        "urls": [
            libsvm_url("binary", "cod-rna"),
            libsvm_url("binary", "cod-rna.t"),
            libsvm_url("binary", "cod-rna.r"),
        ],
        "train": "cod-rna",
        "val": "cod-rna.t",
        "test": "cod-rna.r",
        "format": "libsvm",
        "TASK": TASK_CLASS,
        "size": SIZE_MEDIUM,
    },
    "colon-cancer": {
        "url": libsvm_ds_url("binary", "colon-cancer"),
        "urls": [libsvm_url("binary", "colon-cancer.bz2")],
        "train": "colon-cancer",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "covtype.binary": {
        "url": libsvm_ds_url("binary", "covtype.binary"),
        "urls": [libsvm_url("binary", "covtype.libsvm.binary.bz2")],
        "train": "covtype.libsvm.binary",
        "format": "libsvm",
        "TASK": TASK_CLASS,
        "size": SIZE_MEDIUM,
    },
    "covtype.binary.scale": {
        "url": libsvm_ds_url("binary", "covtype.binary"),
        "urls": [libsvm_url("binary", "covtype.libsvm.binary.scale.bz2")],
        "train": "covtype.libsvm.binary.scale",
        "format": "libsvm",
        "TASK": TASK_CLASS,
        "size": SIZE_MEDIUM,
    },
    "diabetes": {
        "url": libsvm_ds_url("binary", "diabetes"),
        "urls": [libsvm_url("binary", "diabetes")],
        "train": "diabetes",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "diabetes_scale": {
        "url": libsvm_ds_url("binary", "diabetes"),
        "urls": [libsvm_url("binary", "diabetes_scale")],
        "train": "diabetes_scale",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "duke-breast-cancer": {
        "url": libsvm_ds_url("binary", "duke%20breast-cancer"),
        "urls": [
            libsvm_url("binary", "duke.tr.bz2"),
            libsvm_url("binary", "duke.val.bz2"),
        ],
        "train": "duke.tr",
        "val": "duke.val",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "fourclass": {
        "url": libsvm_ds_url("binary", "fourclass"),
        "urls": [libsvm_url("binary", "fourclass")],
        "train": "fourclass",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "fourclass_scale": {
        "url": libsvm_ds_url("binary", "fourclass"),
        "urls": [libsvm_url("binary", "fourclass_scale")],
        "train": "fourclass_scale",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "german.numer": {
        "url": libsvm_ds_url("binary", "german.numer"),
        "urls": [libsvm_url("binary", "german.numer")],
        "train": "german.numer",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "german.numer_scale": {
        "url": libsvm_ds_url("binary", "german.numer"),
        "urls": [libsvm_url("binary", "german.numer_scale")],
        "train": "german.numer_scale",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "gisette": {
        "url": libsvm_ds_url("binary", "gisette"),
        "urls": [
            libsvm_url("binary", "gisette_scale.bz2"),
            libsvm_url("binary", "gisette_scale.t.bz2"),
        ],
        "train": "gisette_scale",
        "test": "gisette_scale.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
        "size": SIZE_MEDIUM,
    },
    "heart": {
        "url": libsvm_ds_url("binary", "heart"),
        "urls": [libsvm_url("binary", "heart")],
        "train": "heart",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "heart_scale": {
        "url": libsvm_ds_url("binary", "heart"),
        "urls": [libsvm_url("binary", "heart_scale")],
        "train": "heart_scale",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "ijcnn1": {
        "url": libsvm_ds_url("binary", "ijcnn1"),
        "urls": [
            libsvm_url("binary", "ijcnn1.tr.bz2"),
            libsvm_url("binary", "ijcnn1.val.bz2"),
            libsvm_url("binary", "ijcnn1.t.bz2"),
        ],
        "train": "ijcnn1.tr",
        "val": "ijcnn1.val",
        "test": "ijcnn1.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "ionosphere": {
        "url": libsvm_ds_url("binary", "ionosphere"),
        "urls": [libsvm_url("binary", "ionosphere_scale")],
        "train": "ionosphere_scale",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "leukemia": {
        "url": libsvm_ds_url("binary", "leukemia"),
        "urls": [libsvm_url("binary", "leu.bz2"), libsvm_url("binary", "leu.t.bz2")],
        "train": "leu",
        "test": "leu.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "madelon": {
        "url": libsvm_ds_url("binary", "madelon"),
        "urls": [libsvm_url("binary", "madelon"), libsvm_url("binary", "madelon.t")],
        "train": "madelon",
        "test": "madelon.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "mushrooms": {
        "url": libsvm_ds_url("binary", "mushrooms"),
        "urls": [libsvm_url("binary", "mushrooms")],
        "train": "mushrooms",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "news20.binary": {
        "url": libsvm_ds_url("binary", "news20.binary"),
        "urls": [libsvm_url("binary", "news20.binary.bz2")],
        "train": "news20.binary",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "phishing": {
        "url": libsvm_ds_url("binary", "phishing"),
        "urls": [libsvm_url("binary", "phishing")],
        "train": "phishing",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "rcv1.binary": {
        "url": libsvm_ds_url("binary", "rcv1.binary"),
        "urls": [
            libsvm_url("binary", "rcv1_train.binary.bz2"),
            libsvm_url("binary", "rcv1_test.binary.bz2"),
        ],
        "train": "rcv1_train.binary",
        "test": "rcv1_test.binary",
        "format": "libsvm",
        "TASK": TASK_CLASS,
        "size": SIZE_MEDIUM,
    },
    "real-sim": {
        "url": libsvm_ds_url("binary", "real-sim"),
        "urls": [libsvm_url("binary", "real-sim.bz2")],
        "train": "real-sim",
        "format": "libsvm",
        "TASK": TASK_CLASS,
        "size": SIZE_LARGE,
    },
    "skin_nonskin": {
        "url": libsvm_ds_url("binary", "skin_nonskin"),
        "urls": [libsvm_url("binary", "skin_nonskin")],
        "train": "skin_nonskin",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "splice": {
        "url": libsvm_ds_url("binary", "splice"),
        "urls": [libsvm_url("binary", "splice"), libsvm_url("binary", "splice.t")],
        "train": "splice",
        "test": "splice.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "sonar": {
        "url": libsvm_ds_url("binary", "sonar"),
        "urls": [libsvm_url("binary", "sonar_scale")],
        "train": "sonar_scale",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "svmguide1": {
        "url": libsvm_ds_url("binary", "svmguide1"),
        "urls": [
            libsvm_url("binary", "svmguide1"),
            libsvm_url("binary", "svmguide1.t"),
        ],
        "train": "svmguide1",
        "test": "svmguide1.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "svmguide3": {
        "url": libsvm_ds_url("binary", "svmguide3"),
        "urls": [
            libsvm_url("binary", "svmguide3"),
            libsvm_url("binary", "svmguide3.t"),
        ],
        "train": "svmguide3",
        "test": "svmguide3.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "w1a": {
        "url": libsvm_ds_url("binary", "w1a"),
        "urls": [libsvm_url("binary", "w1a"), libsvm_url("binary", "w1a.t")],
        "train": "w1a",
        "test": "w1a.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "w2a": {
        "url": libsvm_ds_url("binary", "w2a"),
        "urls": [libsvm_url("binary", "w2a"), libsvm_url("binary", "w2a.t")],
        "train": "w2a",
        "test": "w2a.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "w3a": {
        "url": libsvm_ds_url("binary", "w3a"),
        "urls": [libsvm_url("binary", "w3a"), libsvm_url("binary", "w3a.t")],
        "train": "w3a",
        "test": "w3a.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "w4a": {
        "url": libsvm_ds_url("binary", "w4a"),
        "urls": [libsvm_url("binary", "w4a"), libsvm_url("binary", "w4a.t")],
        "train": "w4a",
        "test": "w4a.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "w5a": {
        "url": libsvm_ds_url("binary", "w5a"),
        "urls": [libsvm_url("binary", "w5a"), libsvm_url("binary", "w5a.t")],
        "train": "w5a",
        "test": "w5a.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "w6a": {
        "url": libsvm_ds_url("binary", "w6a"),
        "urls": [libsvm_url("binary", "w6a"), libsvm_url("binary", "w6a.t")],
        "train": "w6a",
        "test": "w6a.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "w7a": {
        "url": libsvm_ds_url("binary", "w7a"),
        "urls": [libsvm_url("binary", "w7a"), libsvm_url("binary", "w7a.t")],
        "train": "w7a",
        "test": "w7a.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "w8a": {
        "url": libsvm_ds_url("binary", "w8a"),
        "urls": [libsvm_url("binary", "w8a"), libsvm_url("binary", "w8a.t")],
        "train": "w8a",
        "test": "w8a.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "abalone": {
        "url": libsvm_ds_url("binary", "abalone"),
        "urls": [
            libsvm_url("regression", "abalone"),
        ],
        "train": "abalone",
        "format": "libsvm",
        "TASK": TASK_REG,
    },
    "abalone_scale": {
        "url": libsvm_ds_url("binary", "abalone"),
        "urls": [
            libsvm_url("regression", "abalone_scale"),
        ],
        "train": "abalone_scale",
        "format": "libsvm",
        "TASK": TASK_REG,
    },
    "bodyfat": {
        "url": libsvm_ds_url("binary", "bodyfat"),
        "urls": [
            libsvm_url("regression", "bodyfat"),
        ],
        "train": "bodyfat",
        "format": "libsvm",
        "TASK": TASK_REG,
    },
    "bodyfat_scale": {
        "url": libsvm_ds_url("binary", "bodyfat"),
        "urls": [
            libsvm_url("regression", "bodyfat_scale"),
        ],
        "train": "bodyfat_scale",
        "format": "libsvm",
        "TASK": TASK_REG,
    },
    "cadata": {
        "url": libsvm_ds_url("binary", "cadata"),
        "urls": [
            libsvm_url("regression", "cadata"),
        ],
        "train": "cadata",
        "format": "libsvm",
        "TASK": TASK_REG,
    },
    "cpusmall": {
        "url": libsvm_ds_url("binary", "cpusmall"),
        "urls": [
            libsvm_url("regression", "cpusmall"),
        ],
        "train": "cpusmall",
        "format": "libsvm",
        "TASK": TASK_REG,
    },
    "cpusmall_scale": {
        "url": libsvm_ds_url("binary", "cpusmall"),
        "urls": [
            libsvm_url("regression", "cpusmall_scale"),
        ],
        "train": "cpusmall_scale",
        "format": "libsvm",
        "TASK": TASK_REG,
    },
    "SVHN": {
        "url": libsvm_ds_url("multiclass", "SVHN"),
        "urls": [
            libsvm_url("multiclass", "SVHN.xz"),
            libsvm_url("multiclass", "SVHN.t.xz"),
        ],
        "train": "SVHN",
        "test": "SVHN.t",
        "format": "libsvm",
        "TASK": TASK_MULTICLASS,
    },
    "cifar10": {
        "url": libsvm_ds_url("multiclass", "cifar10"),
        "urls": [
            libsvm_url("multiclass", "cifar10.bz2"),
            libsvm_url("multiclass", "cifar10.t.bz2"),
        ],
        "train": "cifar10",
        "test": "cifar10.t",
        "format": "libsvm",
        "TASK": TASK_MULTICLASS,
    },
    "criteo": {
        "url": libsvm_ds_url("multiclass", "cifar10"),
        "urls": [
            libsvm_url("binary", "criteo.kaggle2014.svm.tar.xz"),
        ],
        "train": "criteo.kaggle2014.svm/train.txt.svm",
        "test": "criteo.kaggle2014.svm/test.txt.svm",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "webspam": {
        "url": libsvm_ds_url("binary", "webspam"),
        "urls": [
            libsvm_url("binary", "webspam_wc_normalized_trigram.svm.xz"),
        ],
        "train": "criteo.kaggle2014.svm/train.txt.svm",
        "test": "criteo.kaggle2014.svm/test.txt.svm",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "kdd2010raw": {
        "url": libsvm_ds_url("binary", "kdd2010 raw version (bridge to algebra)"),
        "urls": [
            libsvm_url("binary", "kddb-raw-libsvm.bz2"),
            libsvm_url("binary", "kddb-raw-libsvm.t.bz2"),
        ],
        "train": "kddb-raw-libsvm",
        "test": "kddb-raw-libsvm.t",
        "format": "libsvm",
        "TASK": TASK_CLASS,
    },
    "E2006-log1p": {
        "url": libsvm_ds_url("binary", "E2006-log1p"),
        "urls": [
            libsvm_url("regression", "log1p.E2006.train.bz2"),
            libsvm_url("regression", "log1p.E2006.test.bz2"),
        ],
        "train": "log1p.E2006.train",
        "test": "log1p.E2006.test",
        "format": "libsvm",
        "TASK": TASK_REG,
    },
    "E2006-E2006-tfidf": {
        "url": libsvm_ds_url("binary", "E2006-tfidf"),
        "urls": [
            libsvm_url("regression", "E2006.train.bz2"),
            libsvm_url("regression", "E2006.test.bz2"),
        ],
        "train": "E2006.train",
        "test": "E2006.test",
        "format": "libsvm",
        "TASK": TASK_REG,
    },
    "eunite2001": {
        "url": libsvm_ds_url("binary", "eunite2001"),
        "urls": [
            libsvm_url("regression", "eunite2001"),
            libsvm_url("regression", "eunite2001.t"),
        ],
        "train": "eunite2001",
        "test": "eunite2001.t",
        "format": "libsvm",
        "TASK": TASK_REG,
    },
    "mg": {
        "url": libsvm_ds_url("binary", "mg"),
        "urls": [
            libsvm_url("regression", "mg"),
        ],
        "train": "mg",
        "format": "libsvm",
        "TASK": TASK_REG,
    },
    "mg_scale": {
        "url": libsvm_ds_url("binary", "mg"),
        "urls": [
            libsvm_url("regression", "mg_scale"),
        ],
        "train": "mg_scale",
        "format": "libsvm",
        "TASK": TASK_REG,
    },
    "mpg": {
        "url": libsvm_ds_url("binary", "mpg"),
        "urls": [
            libsvm_url("regression", "mpg"),
        ],
        "train": "mpg",
        "format": "libsvm",
        "TASK": TASK_REG,
    },
    "mpg_scale": {
        "url": libsvm_ds_url("binary", "mpg"),
        "urls": [
            libsvm_url("regression", "mpg_scale"),
        ],
        "train": "mpg_scale",
        "format": "libsvm",
        "TASK": TASK_REG,
    },
    "pyrim": {
        "url": libsvm_ds_url("binary", "pyrim"),
        "urls": [
            libsvm_url("regression", "pyrim"),
        ],
        "train": "pyrim",
        "format": "libsvm",
        "TASK": TASK_REG,
    },
    "pyrim_scale": {
        "url": libsvm_ds_url("binary", "pyrim"),
        "urls": [
            libsvm_url("regression", "pyrim_scale"),
        ],
        "train": "pyrim_scale",
        "format": "libsvm",
        "TASK": TASK_REG,
    },
    "space_ga": {
        "url": libsvm_ds_url("binary", "space_ga"),
        "urls": [
            libsvm_url("regression", "space_ga"),
        ],
        "train": "space_ga",
        "format": "libsvm",
        "TASK": TASK_REG,
    },
    "space_ga_scale": {
        "url": libsvm_ds_url("binary", "space_ga"),
        "urls": [
            libsvm_url("regression", "space_ga_scale"),
        ],
        "train": "space_ga_scale",
        "format": "libsvm",
        "TASK": TASK_REG,
    },
    "triazines": {
        "url": libsvm_ds_url("binary", "triazines"),
        "urls": [
            libsvm_url("regression", "triazines"),
        ],
        "train": "triazines",
        "format": "libsvm",
        "TASK": TASK_REG,
    },
    "triazines_scale": {
        "url": libsvm_ds_url("binary", "triazines"),
        "urls": [
            libsvm_url("regression", "triazines_scale"),
        ],
        "train": "triazines_scale",
        "format": "libsvm",
        "TASK": TASK_REG,
    },
    "YearPredictionMSD": {
        "url": libsvm_ds_url("binary", "YearPredictionMSD"),
        "urls": [
            libsvm_url("regression", "YearPredictionMSD.bz2"),
            libsvm_url("regression", "YearPredictionMSD.t.bz2"),
        ],
        "train": "YearPredictionMSD",
        "test": "YearPredictionMSD.t",
        "format": "libsvm",
        "TASK": TASK_REG,
    },
    "yacht": {
        "url": uci_url("Yacht+Hydrodynamics"),
        "urls": [uci_ds_url("00243/yacht_hydrodynamics.data")],
        "train": "yacht_hydrodynamics.data",
        "format": "uci",
        "TASK": TASK_REG,
    },
    "boston-housing": {
        "url": skl_url("load_boston"),
        "skl_loader": "load_boston",
        "format": "skl",
        "TASK": TASK_REG,
    },
    "california-housing": {
        "url": skl_url("fetch_california_housing"),
        "skl_loader": "fetch_california_housing",
        "format": "skl",
        "TASK": TASK_REG,
    },
    "concrete": {
        "url": uci_url("Concrete+Compressive+Strength"),
        "urls": [uci_ds_url("concrete/compressive/Concrete_Data.xls")],
        "train": "Concrete_Data.xls",
        "format": "uci",
        "TASK": TASK_REG,
    },
    "energy": {
        "url": uci_url("Energy+efficiency"),
        "urls": [uci_ds_url("00242/ENB2012_data.xlsx")],
        "features": slice(None, -2),
        "target": -2,
        "train": "ENB2012_data.xlsx",
        "format": "uci",
        "TASK": TASK_REG,
    },
    "naval-propulsion": {
        "url": uci_url("Condition+Based+Maintenance+of+Naval+Propulsion+Plants"),
        "urls": [uci_ds_url("00316/UCI%20CBM%20Dataset.zip")],
        "features": slice(None, -2),
        "target": -2,
        "train": "UCI CBM Dataset/data.txt",
        "format": "uci",
        "TASK": TASK_REG,
    },
    "power-plant": {
        "url": uci_url("Combined+Cycle+Power+Plant"),
        "urls": [uci_ds_url("00294/CCPP.zip")],
        "train": "CCPP/Folds5x2_pp.xlsx",
        "format": "uci",
        "TASK": TASK_REG,
    },
    "digits": {
        "url": skl_url("load_digits"),
        "skl_loader": "load_digits",
        "format": "skl",
        "TASK": TASK_CLASS,
    },
    "faithful": {
        "url": "http://www.stat.cmu.edu/~larry/all-of-statistics/=data/faithful.dat",
        "train": "faithful.dat",
        "format": "other",
        "TASK": TASK_CLU,
    },
    "movielens-100k": {
        "url": "https://files.grouplens.org/datasets/movielens/ml-100k.zip",
        "subfolder": "ml-100k",
        "train": "u.data",
        "format": "other",
        "TASK": TASK_REC,
        "size": SIZE_MEDIUM,
    },
    "movielens-1m": {
        "url": "https://files.grouplens.org/datasets/movielens/ml-1m.zip",
        "subfolder": "ml-1m",
        "train": "ratings.dat",
        "format": "other",
        "TASK": TASK_REC,
        "size": SIZE_LARGE,
    },
}
