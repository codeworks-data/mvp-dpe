class Config:
    def __init__(self):
        self.FOLDER_NAME = "data"
        self.ZIP_FILE = "data_sample.zip"
        self.FILE_NAME = "dpe_5.csv"
        self.vars_to_drop = [
            'numero_dpe', 'nom_methode_dpe',
            'usr_diagnostiqueur_id', 'usr_logiciel_id', 'version_methode_dpe',
            'nom_methode_etude_thermique', 'version_methode_etude_thermique',
            'date_arrete_tarifs_energies',
            'commentaires_ameliorations_recommandations',
            'explication_personnalisee',
            'tr012_categorie_erp_id', 'tr001_modele_dpe_id',
            'tr013_type_erp_id', 'tv016_departement_id',
            'commune', 'arrondissement', 'type_voie',
            'nom_rue', 'numero_rue', 'batiment', 'escalier',
            'etage', 'porte', 'code_postal', 'code_insee_commune',
            'numero_lot', 'etat_avancement', 'organisme_certificateur',
            'adresse_organisme_certificateur', 'dpe_vierge',
            'est_efface', 'date_reception_dpe'
        ]

        self.vars_high_missing_rate = [
            'type_vitrage_verriere', 'partie_batiment',
            'surface_commerciale_contractuelle', 'secteur_activite',
        ]

        self.vars_hightly_correlated = ['nombre_boutiques', 'surface_thermique_lot']
        self.min_year = 2000
        self.max_year = 2020
