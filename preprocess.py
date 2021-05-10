import os
import numpy as np
import pandas as pd
from config import Config

cfg = Config()

data = pd.read_csv(os.path.join(cfg.FOLDER_NAME, cfg.FILE_NAME), decimal='.', low_memory=False)

data1 = data.drop(cfg.vars_to_drop, axis=1)

data2 = data1.drop(cfg.vars_high_missing_rate, axis=1)

data3 = data2.dropna(inplace=True)

data4 = data3.drop(cfg.vars_hightly_correlated, axis=1)

