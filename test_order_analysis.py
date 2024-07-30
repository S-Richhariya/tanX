import unittest
import pandas as pd
from order_analysis import (
    load_data, total_revenue_by_month,
    total_revenue_by_product, total_revenue_by_customer,
    top_customers_by_revenue
)

class TestOrderAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = pd.DataFrame({
            'order_id': [1, 2, 3, 4],
            'customer_id': [1, 2, 1, 3],
            'order_date': ['2023-07-01', '2023-07-01', '2023-07-15', '2023-08-01'],
            'product_id': [101, 102, 101, 103],
            'product_name': ['Product A', 'Product B', 'Product A', 'Product C'],
            'product_price': [10.0, 20.0, 10.0, 30.0],
            'quantity': [1, 2, 3, 1]
        })
        cls.data['order_date'] = pd.to_datetime(cls.data['order_date'])
        cls.data['total_price'] = cls.data['product_price'] * cls.data['quantity']

    def test_total_revenue_by_month(self):
        expected = pd.Series([80.0, 30.0], index=[pd.Period('2023-07', 'M'), pd.Period('2023-08', 'M')], name='total_price')
        result = total_revenue_by_month(self.data)
        pd.testing.assert_series_equal(result, expected, check_names=False)

    def test_total_revenue_by_product(self):
        expected = pd.Series([40.0, 40.0, 30.0], index=['Product A', 'Product B', 'Product C'], name='total_price')
        result = total_revenue_by_product(self.data)
        pd.testing.assert_series_equal(result, expected, check_names=False)

    def test_total_revenue_by_customer(self):
        expected = pd.Series([40.0, 40.0, 30.0], index=[1, 2, 3], name='total_price')
        result = total_revenue_by_customer(self.data)
        pd.testing.assert_series_equal(result, expected, check_names=False)

    def test_top_customers_by_revenue(self):
        expected = pd.Series([40.0, 40.0, 30.0], index=[1, 2, 3], name='total_price')
        result = top_customers_by_revenue(self.data, top_n=3)
        pd.testing.assert_series_equal(result, expected, check_names=False)

if __name__ == '__main__':
    unittest.main()
