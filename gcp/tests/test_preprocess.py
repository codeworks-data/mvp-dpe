from numpy.testing import assert_equal
from pandas import Series

from gcp.config import Config
from gcp.preprocess import Preprocess
from gcp import utils


class TestPreprocess:

    def test_process(self):
        # GIVEN 5% of the dataset
        cfg: Config = Config()
        data = utils.load_dataset(cfg.FOLDER_NAME, cfg.ZIP_FILE, cfg.FILE_NAME)
        preprocess: Preprocess = Preprocess(input_data=data)

        # WHEN making the data quality
        preprocess.process()

        # THEN the value_counts for the column "annee_visite" should equals the ones expected
        actual: Series = preprocess.df["annee_visite"].value_counts()

        expected = {2019: 69326, 2018: 63990, 2017: 54226, 2016: 49073, 2015: 45034, 2014: 42245,
                    2013: 21818, 2020: 12105, 2012: 43, 2011: 13, 2010: 11, 2009: 9, 2008: 7,
                    2000: 6, 2007: 2, 2005: 1, 2001: 1, 1016: 1}
        assert_equal(actual=actual.to_dict(), desired=expected)


if __name__ == "__main__":
    tp = TestPreprocess()
    tp.test_process()
