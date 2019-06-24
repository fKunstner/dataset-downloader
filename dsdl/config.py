import os

DATA_ROOT = os.path.expanduser(os.path.join("~", "data", "dsdl"))

TASK_CLASS = "Classification"
TASK_REG = "Regression"

SIZE_SMALL = "small"
SIZE_MEDIUM = "medium"
SIZE_LARGE = "large"

AVAILABLE_TASKS = [
    TASK_CLASS,
    TASK_REG
]


def libsvm_url(category, file):
    return "https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/" + category + "/" + file


def libsvm_ds_url(dsname):
    return "https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary.html#" + dsname


DSETS = {
    "a1a": {
        "url": libsvm_ds_url("a1a"),
        "urls": [
            libsvm_url("binary", "a1a"),
            libsvm_url("binary", "a1a.t")
        ],
        "train": "a1a",
        "test": "a1a.t",
        "TASK": TASK_CLASS
    },
    "a2a": {
        "url": libsvm_ds_url("a2a"),
        "urls": [
            libsvm_url("binary", "a2a"),
            libsvm_url("binary", "a2a.t")
        ],
        "train": "a2a",
        "test": "a2a.t",
        "TASK": TASK_CLASS
    },
    "a3a": {
        "url": libsvm_ds_url("a3a"),
        "urls": [
            libsvm_url("binary", "a3a"),
            libsvm_url("binary", "a3a.t")
        ],
        "train": "a3a",
        "test": "a3a.t",
        "TASK": TASK_CLASS
    },
    "a4a": {
        "url": libsvm_ds_url("a4a"),
        "urls": [
            libsvm_url("binary", "a4a"),
            libsvm_url("binary", "a4a.t")
        ],
        "train": "a4a",
        "test": "a4a.t",
        "TASK": TASK_CLASS
    },
    "a5a": {
        "url": libsvm_ds_url("a5a"),
        "urls": [
            libsvm_url("binary", "a5a"),
            libsvm_url("binary", "a5a.t")
        ],
        "train": "a5a",
        "test": "a5a.t",
        "TASK": TASK_CLASS
    },
    "a6a": {
        "url": libsvm_ds_url("a6a"),
        "urls": [
            libsvm_url("binary", "a6a"),
            libsvm_url("binary", "a6a.t")
        ],
        "train": "a6a",
        "test": "a6a.t",
        "TASK": TASK_CLASS
    },
    "a7a": {
        "url": libsvm_ds_url("a7a"),
        "urls": [
            libsvm_url("binary", "a7a"),
            libsvm_url("binary", "a7a.t")
        ],
        "train": "a7a",
        "test": "a7a.t",
        "TASK": TASK_CLASS
    },
    "a8a": {
        "url": libsvm_ds_url("a8a"),
        "urls": [
            libsvm_url("binary", "a8a"),
            libsvm_url("binary", "a8a.t")
        ],
        "train": "a8a",
        "test": "a8a.t",
        "TASK": TASK_CLASS
    },
    "a9a": {
        "url": libsvm_ds_url("a9a"),
        "urls": [
            libsvm_url("binary", "a9a"),
            libsvm_url("binary", "a9a.t")
        ],
        "train": "a9a",
        "test": "a9a.t",
        "TASK": TASK_CLASS
    },
    "australian": {
        "url": libsvm_ds_url("australian"),
        "urls": [
            libsvm_url("binary", "australian"),
        ],
        "train": "australian",
        "TASK": TASK_CLASS
    },
    "australian_scale": {
        "url": libsvm_ds_url("australian"),
        "urls": [
            libsvm_url("binary", "australian_scale"),
        ],
        "train": "australian_scale",
        "TASK": TASK_CLASS
    },
    "breast-cancer": {
        "url": libsvm_ds_url("breast-cancer"),
        "urls": [
            libsvm_url("binary", "breast-cancer"),
        ],
        "train": "breast-cancer",
        "TASK": TASK_CLASS
    },
    "breast-cancer_scale": {
        "url": libsvm_ds_url("breast-cancer"),
        "urls": [
            libsvm_url("binary", "breast-cancer"),
        ],
        "train": "breast-cancer_scale",
        "TASK": TASK_CLASS
    },
    "cod-rna": {
        "url": libsvm_ds_url("cod-rna"),
        "urls": [
            libsvm_url("binary", "cod-rna"),
            libsvm_url("binary", "cod-rna.t"),
            libsvm_url("binary", "cod-rna.r"),
        ],
        "train": "cod-rna",
        "val": "cod-rna.t",
        "test": "cod-rna.r",
        "TASK": TASK_CLASS,
        "size": SIZE_MEDIUM
    },
    "colon-cancer": {
        "url": libsvm_ds_url("colon-cancer"),
        "urls": [
            libsvm_url("binary", "colon-cancer.bz2")
        ],
        "train": "colon-cancer",
        "TASK": TASK_CLASS
    },
    "covtype.binary": {
        "url": libsvm_ds_url("covtype.binary"),
        "urls": [libsvm_url("binary", "covtype.libsvm.binary.bz2")],
        "train": "covtype.libsvm.binary",
        "TASK": TASK_CLASS,
        "size": SIZE_MEDIUM
    },
    "covtype.binary.scale": {
        "url": libsvm_ds_url("covtype.binary"),
        "urls": [libsvm_url("binary", "covtype.libsvm.binary.scale.bz2")],
        "train": "covtype.libsvm.binary.scale",
        "TASK": TASK_CLASS,
        "size": SIZE_MEDIUM
    },
    "criteo": {
        "url": libsvm_ds_url("criteo"),
        "urls": ["https://s3-us-west-2.amazonaws.com/criteo-public-svm-data/criteo.kaggle2014.svm.tar.gz"],
        "train": "criteo.kaggle2014.svm",
        "TASK": TASK_CLASS,
        "size": SIZE_LARGE
    },
    "diabetes": {
        "url": libsvm_ds_url("diabetes"),
        "urls": [libsvm_url("binary", "diabetes")],
        "train": "diabetes",
        "TASK": TASK_CLASS
    },
    "diabetes_scale": {
        "url": libsvm_ds_url("diabetes"),
        "urls": [libsvm_url("binary", "diabetes_scale")],
        "train": "diabetes_scale",
        "TASK": TASK_CLASS
    },
    "duke-breast-cancer": {
        "url": libsvm_ds_url("duke%20breast-cancer"),
        "urls": [
            libsvm_url("binary", "duke.tr.bz2"),
            libsvm_url("binary", "duke.val.bz2")
        ],
        "train": "duke.tr",
        "val": "duke.val",
        "TASK": TASK_CLASS
    },
    "epsilon": {
        "url": libsvm_ds_url("epsilon"),
        "urls": [
            libsvm_url("binary", "epsilon_normalized.bz2"),
            libsvm_url("binary", "epsilon_normalized.t.bz2")
        ],
        "train": "epsilon_normalized",
        "test": "epsilon_normalized.t",
        "TASK": TASK_CLASS,
        "size": SIZE_LARGE
    },
    "fourclass": {
        "url": libsvm_ds_url("fourclass"),
        "urls": [
            libsvm_url("binary", "fourclass"),
        ],
        "train": "fourclass",
        "TASK": TASK_CLASS
    },
    "fourclass_scale": {
        "url": libsvm_ds_url("fourclass"),
        "urls": [
            libsvm_url("binary", "fourclass_scale"),
        ],
        "train": "fourclass_scale",
        "TASK": TASK_CLASS
    },
    "german.numer": {
        "url": libsvm_ds_url("german.numer"),
        "urls": [
            libsvm_url("binary", "german.numer"),
        ],
        "train": "german.numer",
        "TASK": TASK_CLASS
    },
    "german.numer_scale": {
        "url": libsvm_ds_url("german.numer"),
        "urls": [
            libsvm_url("binary", "german.numer_scale"),
        ],
        "train": "german.numer_scale",
        "TASK": TASK_CLASS
    },
    "gisette": {
        "url": libsvm_ds_url("gisette"),
        "urls": [
            libsvm_url("binary", "gisette_scale.bz2"),
            libsvm_url("binary", "gisette_scale.t.bz2"),
        ],
        "train": "gisette_scale",
        "test": "gisette_scale.t",
        "TASK": TASK_CLASS,
        "size": SIZE_MEDIUM
    },
    "heart": {
        "url": libsvm_ds_url("heart"),
        "urls": [
            libsvm_url("binary", "heart"),
        ],
        "train": "heart",
        "TASK": TASK_CLASS,
    },
    "heart_scale": {
        "url": libsvm_ds_url("heart"),
        "urls": [
            libsvm_url("binary", "heart_scale"),
        ],
        "train": "heart_scale",
        "TASK": TASK_CLASS,
    },
    "higgs": {
        "url": libsvm_ds_url("higgs"),
        "urls": [
            libsvm_url("binary", "HIGGS.bz2"),
        ],
        "train": "HIGGS",
        "TASK": TASK_CLASS,
        "size": SIZE_LARGE
    },
    "ijcnn1": {
        "url": libsvm_ds_url("ijcnn1"),
        "urls": [
            libsvm_url("binary", "ijcnn1.tr.bz2"),
            libsvm_url("binary", "ijcnn1.val.bz2"),
            libsvm_url("binary", "ijcnn1.t.bz2"),
        ],
        "train": "ijcnn1.tr",
        "val": "ijcnn1.val",
        "test": "ijcnn1.t",
        "TASK": TASK_CLASS,
    },
    "ionosphere": {
        "url": libsvm_ds_url("ionosphere"),
        "urls": [
            libsvm_url("binary", "ionosphere_scale"),
        ],
        "train": "ionosphere_scale",
        "TASK": TASK_CLASS,
    },
    "kdd2010-algebra": {
        "url": libsvm_ds_url("kdd2010-algebra"),
        "urls": [
            libsvm_url("binary", "kdda.bz2"),
            libsvm_url("binary", "kdda.t.bz2"),
        ],
        "train": "kdda",
        "test": "kdda.t",
        "TASK": TASK_CLASS,
        "size": SIZE_MEDIUM
    },
    "kdd2010-bridge-to-algebra": {
        "url": libsvm_ds_url("kdd2010-bridge-to-algebra"),
        "urls": [
            libsvm_url("binary", "kddb.bz2"),
            libsvm_url("binary", "kddb.t.bz2"),
        ],
        "train": "kddb",
        "test": "kddb.t",
        "TASK": TASK_CLASS,
        "size": SIZE_MEDIUM
    },
    "kdd2010-bridge-to-algebra-raw": {
        "url": libsvm_ds_url("kdd2010-bridge-to-algebra-raw"),
        "urls": [
            libsvm_url("binary", "kddb-raw-libsvm.bz2"),
            libsvm_url("binary", "kddb-raw-libsvm.t.bz2"),
        ],
        "train": "kddb-raw-libsvm",
        "test": "kddb-raw-libsvm.t",
        "TASK": TASK_CLASS,
        "size": SIZE_MEDIUM
    },
    "kdd2012": {
        "url": libsvm_ds_url("kdd2012"),
        "urls": [
            libsvm_url("binary", "kdd12.tr.bz2"),
            libsvm_url("binary", "kdd12.val.bz2"),
        ],
        "train": "kdd12.tr",
        "val": "kdd12.val",
        "TASK": TASK_CLASS,
        "size": SIZE_MEDIUM
    },
    "leukemia": {
        "url": libsvm_ds_url("leukemia"),
        "urls": [
            libsvm_url("binary", "leu.bz2"),
            libsvm_url("binary", "leu.t.bz2"),
        ],
        "train": "leu",
        "test": "leu.t",
        "TASK": TASK_CLASS,
    },
    "madelon": {
        "url": libsvm_ds_url("madelon"),
        "urls": [
            libsvm_url("binary", "madelon"),
            libsvm_url("binary", "madelon.t"),
        ],
        "train": "madelon",
        "test": "madelon.t",
        "TASK": TASK_CLASS,
    },
    "mushrooms": {
        "url": libsvm_ds_url("mushrooms"),
        "urls": [
            libsvm_url("binary", "mushrooms"),
        ],
        "train": "mushrooms",
        "TASK": TASK_CLASS,
    },
    "news20.binary": {
        "url": libsvm_ds_url("news20.binary"),
        "urls": [
            libsvm_url("binary", "news20.binary.bz2"),
        ],
        "train": "news20.binary",
        "TASK": TASK_CLASS,
        "size": SIZE_LARGE
    },
    "phishing": {
        "url": libsvm_ds_url("phishing"),
        "urls": [
            libsvm_url("binary", "phishing"),
        ],
        "train": "phishing",
        "TASK": TASK_CLASS,
    },
    "rcv1.binary": {
        "url": libsvm_ds_url("rcv1.binary"),
        "urls": [
            libsvm_url("binary", "rcv1_train.binary.bz2"),
            libsvm_url("binary", "rcv1_test.binary.bz2"),
        ],
        "train": "rcv1_train.binary",
        "test": "rcv1_test.binary",
        "TASK": TASK_CLASS,
        "size": SIZE_MEDIUM,
    },
    "real-sim": {
        "url": libsvm_ds_url("real-sim"),
        "urls": [
            libsvm_url("binary", "real-sim.bz2"),
        ],
        "train": "real-sim",
        "TASK": TASK_CLASS,
        "size": SIZE_LARGE
    },
    "skin_nonskin": {
        "url": libsvm_ds_url("skin_nonskin"),
        "urls": [
            libsvm_url("binary", "skin_nonskin"),
        ],
        "train": "skin_nonskin",
        "TASK": TASK_CLASS,
    },
    "splice": {
        "url": libsvm_ds_url("splice"),
        "urls": [
            libsvm_url("binary", "splice"),
            libsvm_url("binary", "splice.t"),
        ],
        "train": "splice",
        "test": "splice.t",
        "TASK": TASK_CLASS,
    },
    "splice_site": {
        "url": libsvm_ds_url("splice_site"),
        "urls": [
            libsvm_url("binary", "splice_site.xz"),
            libsvm_url("binary", "splice_site.t.xz"),
        ],
        "train": "splice_site",
        "test": "splice_site.t",
        "TASK": TASK_CLASS,
        "size": SIZE_LARGE
    },
    "sonar": {
        "url": libsvm_ds_url("sonar"),
        "urls": [
            libsvm_url("binary", "sonar_scale"),
        ],
        "train": "sonar_scale",
        "TASK": TASK_CLASS,
    },
    "SUSY": {
        "url": libsvm_ds_url("SUSY"),
        "urls": [
            libsvm_url("binary", "SUSY.bz2"),
        ],
        "train": "SUSY",
        "TASK": TASK_CLASS,
        "size": SIZE_MEDIUM
    },
    "svmguide1": {
        "url": libsvm_ds_url("svmguide1"),
        "urls": [
            libsvm_url("binary", "svmguide1"),
            libsvm_url("binary", "svmguide1.t"),
        ],
        "train": "svmguide1",
        "test": "svmguide1.t",
        "TASK": TASK_CLASS,
    },
    "svmguide3": {
        "url": libsvm_ds_url("svmguide3"),
        "urls": [
            libsvm_url("binary", "svmguide3"),
            libsvm_url("binary", "svmguide3.t"),
        ],
        "train": "svmguide3",
        "test": "svmguide3.t",
        "TASK": TASK_CLASS,
    },
    "w1a": {
        "url": libsvm_ds_url("w1a"),
        "urls": [
            libsvm_url("binary", "w1a"),
            libsvm_url("binary", "w1a.t"),
        ],
        "train": "w1a",
        "test": "w1a.t",
        "TASK": TASK_CLASS,
    },
    "w2a": {
        "url": libsvm_ds_url("w2a"),
        "urls": [
            libsvm_url("binary", "w2a"),
            libsvm_url("binary", "w2a.t"),
        ],
        "train": "w2a",
        "test": "w2a.t",
        "TASK": TASK_CLASS,
    },
    "w3a": {
        "url": libsvm_ds_url("w3a"),
        "urls": [
            libsvm_url("binary", "w3a"),
            libsvm_url("binary", "w3a.t"),
        ],
        "train": "w3a",
        "test": "w3a.t",
        "TASK": TASK_CLASS,
    },
    "w4a": {
        "url": libsvm_ds_url("w4a"),
        "urls": [
            libsvm_url("binary", "w4a"),
            libsvm_url("binary", "w4a.t"),
        ],
        "train": "w4a",
        "test": "w4a.t",
        "TASK": TASK_CLASS,
    },
    "w5a": {
        "url": libsvm_ds_url("w5a"),
        "urls": [
            libsvm_url("binary", "w5a"),
            libsvm_url("binary", "w5a.t"),
        ],
        "train": "w5a",
        "test": "w5a.t",
        "TASK": TASK_CLASS,
    },
    "w6a": {
        "url": libsvm_ds_url("w6a"),
        "urls": [
            libsvm_url("binary", "w6a"),
            libsvm_url("binary", "w6a.t"),
        ],
        "train": "w6a",
        "test": "w6a.t",
        "TASK": TASK_CLASS,
    },
    "w7a": {
        "url": libsvm_ds_url("w7a"),
        "urls": [
            libsvm_url("binary", "w7a"),
            libsvm_url("binary", "w7a.t"),
        ],
        "train": "w7a",
        "test": "w7a.t",
        "TASK": TASK_CLASS,
    },
    "w8a": {
        "url": libsvm_ds_url("w8a"),
        "urls": [
            libsvm_url("binary", "w8a"),
            libsvm_url("binary", "w8a.t"),
        ],
        "train": "w8a",
        "test": "w8a.t",
        "TASK": TASK_CLASS,
    },
}
