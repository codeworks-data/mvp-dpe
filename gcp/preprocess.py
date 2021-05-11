import pandas as pd

from gcp import utils
from gcp.config import Config


class Preprocess:
    def __init__(self, input_data: pd.DataFrame):
        self.cfg = Config()
        self.input_data = input_data
        self.df: pd.DataFrame = pd.DataFrame()

    def __clean_dataset(self):
        relevant_df = self.input_data.drop(self.cfg.vars_to_drop, axis=1)
        no_high_missing_df = relevant_df.drop(self.cfg.vars_high_missing_rate, axis=1)
        no_high_missing_df.dropna(inplace=True)
        df = no_high_missing_df.drop(self.cfg.vars_hightly_correlated, axis=1)
        self.df = df

    def __data_quality(self):
        df = self.df
        df.loc[((df.annee_construction < self.cfg.min_year)
                | (df.annee_construction > self.cfg.max_year)), 'annee_construction'] \
            = df.loc[((df.annee_construction > self.cfg.min_year)
                      & (df.annee_construction < self.cfg.max_year)),
                     'annee_construction'].median()

        df['annee_visite'] = df.apply(lambda row: int(row['date_visite_diagnostiqueur'][:4])
        if 2000 < int(row['date_visite_diagnostiqueur'][:4]) < self.cfg.max_year
        else int(row['date_etablissement_dpe'][:4]), axis=1)

        df['annee_visite'] = df.apply(lambda row: int(row['date_visite_diagnostiqueur'][:4])
        if 2000 < int(row['date_visite_diagnostiqueur'][:4]) < self.cfg.max_year
           and int(row['date_visite_diagnostiqueur'][:4]) < int(row['date_etablissement_dpe'][:4])
        else int(row['date_etablissement_dpe'][:4]), axis=1)
        self.df = df

    def process(self):
        self.__clean_dataset()
        self.__data_quality()


def main():
    cfg: Config = Config()
    data = utils.load_dataset(cfg.FOLDER_NAME, cfg.ZIP_FILE, cfg.FILE_NAME)
    preprocess: Preprocess = Preprocess(input_data=data)
    preprocess.process()


if __name__ == "__main__":
    main()
