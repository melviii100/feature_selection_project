from ..build import percentile_k_features
from unittest import TestCase
from inspect import getargspec
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')


class TestPercentile_k_features(TestCase):
    def test_percentile_k_features(self):
        # Input parameters tests
        args = getargspec(percentile_k_features)
        self.assertEqual(len(args[0]), 5, "Expected arguments %d, Given %d" % (5, len(args[0])))
        self.assertEqual((args[3] == (None,)), True, "Expected default values do not match given default values")

        # Return data types
        expected = ['OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea', 'TotalBsmtSF', '1stFlrSF', 'FullBath',
                    'TotRmsAbvGrd',
                    'YearBuilt',
                    'YearRemodAdd']

        predictors = list(data.columns.values)[:-1]
        target = 'SalePrice'
        top_features = percentile_k_features(data, predictors, target, 10)
        self.assertIsInstance(top_features, list,
                              "Expected data type for return value is `List`, you are returning %s" % (
                                  type(top_features)))

        # Return values tests
        self.assertEqual(top_features, expected, "Expected list of variables does not match returned list of variables")
