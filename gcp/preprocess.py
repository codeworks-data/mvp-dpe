import pandas as pd
import numpy as np

from gcp import utils
from gcp.config import Config


class Preprocess:
    def __init__(self, input_data: pd.DataFrame):
        self.cfg = Config()
        self.input_data = input_data
        self.df: pd.DataFrame = pd.DataFrame()

    def __clean_dataset(self):
        self.df = self.input_data.drop(self.cfg.vars_to_drop, axis=1)
        self.df = self.df.drop(self.cfg.vars_high_missing_rate, axis=1)
        self.df.dropna(inplace=True)
        self.df.drop(self.cfg.vars_highly_correlated, axis=1, inplace=True)

    def __data_quality_annee_construction(self):
        self.df.loc[((self.df.annee_construction < self.cfg.min_year_construction)
                     | (self.df.annee_construction > self.cfg.max_year)), 'annee_construction'] \
            = self.df.loc[((self.df.annee_construction > self.cfg.min_year_construction)
                           & (self.df.annee_construction < self.cfg.max_year)),
                          'annee_construction'].median()

    def __data_quality_age_batiment(self):
        self.df['annee_visite'] = self.df.apply(
            lambda row: int(row['date_visite_diagnostiqueur'][:4])
            if self.cfg.min_year_diagnostic < int(row['date_visite_diagnostiqueur'][:4])
               < self.cfg.max_year
            else int(row['date_etablissement_dpe'][:4]), axis=1)

        self.df['annee_visite'] = self.df.apply(
            lambda row: int(row['date_visite_diagnostiqueur'][:4])
            if self.cfg.min_year_diagnostic < int(
                row['date_visite_diagnostiqueur'][:4]) < self.cfg.max_year
               and int(row['date_visite_diagnostiqueur'][:4]) < int(
                row['date_etablissement_dpe'][:4])
            else int(row['date_etablissement_dpe'][:4]), axis=1)

        self.df['annee_visite'] = self.df['annee_visite'].replace(1016, 2016)

        self.df['age'] = self.df['annee_visite'] - self.df['annee_construction']
        self.df.loc[(self.df['age'] == -1) | (self.df['age'] == -4), 'age'] = 0
        self.df.drop(self.df.loc[self.df['age'] < 0].index, inplace=True)

    def __data_quality_surface_habitable(self):
        self.df.drop(self.df.loc[self.df['surface_habitable'] > 1000].index, inplace=True)

    def __data_quality_nombre_niveaux(self):
        self.df.drop(self.df.loc[self.df['nombre_niveaux'] > 25].index, inplace=True)

    def __data_quality_code_insee_commune_actualisee(self):
        self.df['code_departement'] = self.df['code_insee_commune_actualise'].str[:2]
        departs = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13',
                   '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                   '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
                   '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52',
                   '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65',
                   '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78',
                   '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91',
                   '92', '93', '94', '95', '96', '97', '2A', '2B']
        self.df = self.df[self.df.code_departement.isin(departs)]

    def __data_quality_surface_parois_verticale_opaques_perditives(self):
        self.df.loc[self.df.surface_parois_verticales_opaques_deperditives < 0,
                    'surface_parois_verticales_opaques_deperditives'] \
            = self.df.surface_parois_verticales_opaques_deperditives * -1

    def __data_quality_surface_planchers_bas_deperditifs(self):
        self.df.loc[
            self.df.surface_planchers_bas_deperditifs < 0, 'surface_planchers_bas_deperditifs'] \
            = self.df.surface_planchers_bas_deperditifs * -1

    def __data_quality_surface_baies_orientees_est_ouest(self):
        self.df.loc[self.df.surface_baies_orientees_est_ouest < 0,
                    'surface_baies_orientees_est_ouest'] \
            = self.df.surface_baies_orientees_est_ouest * -1

    def __data_quality(self):
        self.__data_quality_annee_construction()
        self.__data_quality_age_batiment()
        self.__data_quality_surface_habitable()
        self.__data_quality_nombre_niveaux()
        # en_surface, en_souterrain, presence_verriere: no change
        self.__data_quality_code_insee_commune_actualisee()
        self.__data_quality_surface_parois_verticale_opaques_perditives()
        self.__data_quality_surface_planchers_bas_deperditifs()
        self.__data_quality_surface_baies_orientees_est_ouest()

    def __target_energy_consumption(self):
        self.df.loc[self.df.consommation_energie < 0, 'consommation_energie'] \
            = self.df.consommation_energie * -1
        self.df = self.df.loc[self.df['consommation_energie'] < 500]
        self.df = self.df.loc[self.df['consommation_energie'] != 0]

        x = self.df['consommation_energie']
        conditions = [(x >= 0) & (x <= 50), (x > 50) & (x <= 90), (x > 90) & (x <= 150),
                      (x > 150) & (x <= 230), (x > 230) & (x <= 330), (x > 330) & (x < 450),
                      (x >= 450)]
        choices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.df['classe_consommation_energie'] = np.select(conditions, choices)

        self.df['energie_totale'] = self.df['consommation_energie'] * self.df['surface_habitable']

    def __target_green_house_emission(self):
        self.df = self.df.loc[self.df['estimation_ges'] > 0]
        x = self.df['estimation_ges']
        conditions = [(x > 0) & (x <= 5), (x > 5) & (x <= 10), (x > 10) & (x <= 20),
                      (x > 20) & (x <= 35), (x > 35) & (x <= 55), (x > 55) & (x <= 80), (x > 80)]
        choices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.df['classe_consommation_ges'] = np.select(conditions, choices)

    def __target(self):
        self.__target_energy_consumption()
        self.__target_green_house_emission()

    def process(self):
        self.__clean_dataset()
        self.__data_quality()
        self.__target()


def main():
    cfg: Config = Config()
    data = utils.load_dataset(cfg.FOLDER_NAME, cfg.ZIP_FILE, cfg.FILE_NAME)
    preprocess: Preprocess = Preprocess(input_data=data)
    preprocess.process()


if __name__ == "__main__":
    main()
