import sys
import unittest
from pathlib import Path


CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent
sys.path.insert(0, str(PROJECT_ROOT))

from analysis import (  # type: ignore
    load_sales_data,
    calc_total_revenue,
    revenue_by_region,
    revenue_by_product_line,
    monthly_revenue,
    top_n_product_lines_by_revenue,
)


class TestSalesAnalysis(unittest.TestCase):
    "Simple, readable checks to keep the analysis helpers honest."

    @classmethod
    def setUpClass(cls):
        # Load the sample data once for all tests so we keep things fast.
        csv_path = PROJECT_ROOT / "data" / "sales_data_sample.csv"
        cls.sales = load_sales_data(str(csv_path))

    def test_total_revenue(self):
        total = calc_total_revenue(self.sales)
        # Total SALES from the CSV
        self.assertAlmostEqual(total, 10032628.85, places=2)

    def testRevenueByregion(self):
        result = revenue_by_region(self.sales)
        # Check a few key countries
        self.assertAlmostEqual(result["USA"], 3627982.83, places=2)
        self.assertAlmostEqual(result["France"], 1110916.52, places=2)
        self.assertAlmostEqual(result["Spain"], 1215686.92, places=2)

    def testRevenueByProductLine(self):
        result = revenue_by_product_line(self.sales)
        # These are the known totals for the sample dataset.
        expected = {
            "Classic Cars": 3919615.66,
            "Vintage Cars": 1903150.84,
            "Motorcycles": 1166388.34,
            "Trains": 226243.47,
        }
        for pl, value in expected.items():
            self.assertAlmostEqual(result[pl], value, places=2)

    def testmonthlyrevenuesample(self):
        result = monthly_revenue(self.sales)
        # Spot-check a few months so we know the grouping logic holds up.
        self.assertAlmostEqual(result["2003-11"], 1029837.66, places=2)
        self.assertAlmostEqual(result["2004-06"], 286674.22, places=2)
        self.assertAlmostEqual(result["2005-05"], 457861.06, places=2)

    def testtopnproductlinesbyrevenue(self):
        top3 = top_n_product_lines_by_revenue(self.sales, n=3)
        # We only care about the order of the winners for this check.
        names = [name for name, _ in top3]
        self.assertEqual(names, ["Classic Cars", "Vintage Cars", "Motorcycles"])


if __name__ == "__main__":
    unittest.main()
