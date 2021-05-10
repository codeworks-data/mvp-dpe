import os
import numpy as np
import pandas as pd
from config import Config


cfg = Config()

data = pd.read_csv(os.path.join(cfg.FOLDER_NAME, cfg.FILE_NAME), decimal='.', low_memory=False)

data1 = data.drop(cfg.vars_to_drop, axis=1)

data2 = data1.drop(cfg.vars_high_missing_rate, axis=1)

data2.dropna(inplace=True)

data4 = data2.drop(cfg.vars_hightly_correlated, axis=1)

data4.loc[((data4.annee_construction < cfg.min_year) | (data4.annee_construction > cfg.max_year )),'annee_construction'] = data4.loc[((data4.annee_construction > cfg.min_year) & (data4.annee_construction < cfg.max_year )),'annee_construction'].median()

data4['annee_visite'] = data4.apply(lambda row: int(row['date_visite_diagnostiqueur'][:4])
 if int(row['date_visite_diagnostiqueur'][:4]) > 2000 and int(row['date_visite_diagnostiqueur'][:4]) < cfg.max_year
else int(row['date_etablissement_dpe'][:4]), axis=1)

data4['annee_visite'] = data4.apply(lambda row: int(row['date_visite_diagnostiqueur'][:4])
 if int(row['date_visite_diagnostiqueur'][:4]) > 2000 and int(row['date_visite_diagnostiqueur'][:4]) < cfg.max_year and int(row['date_visite_diagnostiqueur'][:4])<int(row['date_etablissement_dpe'][:4])
 else int(row['date_etablissement_dpe'][:4]), axis=1)


print(data4['annee_visite'].value_counts())


