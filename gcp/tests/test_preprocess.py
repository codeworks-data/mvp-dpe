from numpy.testing import assert_equal

from gcp import utils
from gcp.config import Config
from gcp.preprocess import Preprocess


class TestPreprocess:

    def test_process(self):
        # GIVEN 5% of the dataset
        cfg: Config = Config()
        data = utils.load_dataset(cfg.FOLDER_NAME, cfg.ZIP_FILE, cfg.FILE_NAME)
        preprocess: Preprocess = Preprocess(input_data=data)

        # WHEN processing the data
        preprocess.process()

        # THEN the value_counts for the column "classe_consommation_ges"
        # should equals the expected ones
        expected = {"C": 66759, "B": 49978, "E": 49562, "D": 49203, "A": 26262, "F": 24743,
                    "G": 9751}

        actual = preprocess.df['classe_consommation_ges'].value_counts()

        assert_equal(actual=actual.to_dict(), desired=expected)
