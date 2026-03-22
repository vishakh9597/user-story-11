import unittest
import pandas as pd
from src.settlement_engine import generate_settlement

class TestSettlement(unittest.TestCase):

    def test_settlement_only_valid_transactions(self):
        df = pd.DataFrame([
            {"merchant_id":1,"transaction_amount":100,"transaction_status":"VALID"},
            {"merchant_id":1,"transaction_amount":200,"transaction_status":"SUSPICIOUS"}
        ])
        merchants = pd.DataFrame({"merchant_id":[1],"merchant_name":["Test"]})
        self.assertEqual(generate_settlement(df,merchants).iloc[0]["settlement_amount"],100)

    def test_settlement_amount_calculation(self):
        df = pd.DataFrame([
            {"merchant_id":1,"transaction_amount":100,"transaction_status":"VALID"},
            {"merchant_id":1,"transaction_amount":200,"transaction_status":"VALID"}
        ])
        merchants = pd.DataFrame({"merchant_id":[1],"merchant_name":["Test"]})
        self.assertEqual(generate_settlement(df,merchants).iloc[0]["settlement_amount"],300)