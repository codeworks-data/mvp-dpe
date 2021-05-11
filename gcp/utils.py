import os
import zipfile

import pandas as pd


def load_dataset(folder_name, zip_file, file_name):
    zf = zipfile.ZipFile(os.path.join(folder_name, zip_file))
    return pd.read_csv(zf.open(file_name), decimal='.', low_memory=False)