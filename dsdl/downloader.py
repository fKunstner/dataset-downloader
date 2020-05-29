import os
import os.path
import gzip
import bz2
import lzma
import tarfile
import zipfile
import urllib


from tqdm import tqdm


def gen_bar_updater():
    pbar = tqdm(total=None, leave=False)

    def bar_update(count, block_size, total_size):
        if pbar.total is None and total_size:
            pbar.total = total_size
        progress_bytes = count * block_size
        pbar.update(progress_bytes - pbar.n)

    return bar_update


def download_url(url, fpath):
    print("    Downloading " + url + " to " + fpath)
    urllib.request.urlretrieve(url, fpath, reporthook=gen_bar_updater())


def _is_tar(filename):
    return filename.endswith(".tar")


def _is_targz(filename):
    return filename.endswith(".tar.gz")


def _is_gzip(filename):
    return filename.endswith(".gz") and not filename.endswith(".tar.gz")


def _is_zip(filename):
    return filename.endswith(".zip")


def _is_bz2(filename):
    return filename.endswith(".bz2")


def _is_xz(filename):
    return filename.endswith(".xz")


def extract_archive(folder_path, filename):
    archive_path = os.path.join(folder_path, filename)
    print("    Extracting {} to {}".format(archive_path, folder_path))

    if folder_path is None:
        folder_path = os.path.dirname(archive_path)

    if _is_tar(archive_path):
        with tarfile.open(archive_path, "r") as tar:
            tar.extractall(path=folder_path)
    elif _is_targz(archive_path):
        with tarfile.open(archive_path, "r:gz") as tar:
            tar.extractall(path=folder_path)
    elif _is_gzip(archive_path):
        folder_path = os.path.join(
            folder_path, os.path.splitext(os.path.basename(archive_path))[0]
        )
        with open(folder_path, "wb") as out_f, gzip.GzipFile(archive_path) as zip_f:
            out_f.write(zip_f.read())
    elif _is_zip(archive_path):
        with zipfile.ZipFile(archive_path, "r") as z:
            z.extractall(folder_path)
    elif _is_bz2(archive_path):
        folder_path = os.path.join(
            folder_path, os.path.splitext(os.path.basename(archive_path))[0]
        )
        with open(folder_path, "wb") as out_f, bz2.open(archive_path) as bz2_f:
            out_f.write(bz2_f.read())
    elif _is_xz(archive_path):
        folder_path = os.path.join(
            folder_path, os.path.splitext(os.path.basename(archive_path))[0]
        )
        with open(folder_path, "wb") as out_f, lzma.open(archive_path) as xz_f:
            out_f.write(xz_f.read())
    else:
        print("    - Nothing to extract in {}".format(archive_path))
        return
    os.remove(archive_path)


def download_and_extract(url, download_root):
    download_root = os.path.expanduser(download_root)
    filename = os.path.basename(url)

    fpath = os.path.join(download_root, filename)
    os.makedirs(download_root, exist_ok=True)

    download_url(url, fpath)
    extract_archive(download_root, filename)
