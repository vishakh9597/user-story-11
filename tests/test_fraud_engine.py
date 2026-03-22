import unittest
import pandas as pd
from datetime import datetime
from src.fraud_engine import detect_fraud

class TestFraud(unittest.TestCase):

    def setUp(self):
        self.merchants = pd.DataFrame({"merchant_id":[1],"country":["IN"]})

    def test_high_value_transaction_flag(self):
        df = pd.DataFrame([{"transaction_amount":200000,"merchant_id":1,"customer_id":1,
                            "transaction_time":datetime.now(),"country":"IN","payment_method":"CARD"}])
        self.assertEqual(detect_fraud(df,self.merchants).iloc[0]["fraud_flag"],1)

    def test_cross_border_transaction_flag(self):
        df = pd.DataFrame([{"transaction_amount":100,"merchant_id":1,"customer_id":1,
                            "transaction_time":datetime.now(),"country":"US","payment_method":"CARD"}])
        self.assertIn("CROSS_BORDER", detect_fraud(df,self.merchants).iloc[0]["fraud_reason"])

    def test_crypto_high_value_flag(self):
        df = pd.DataFrame([{"transaction_amount":60000,"merchant_id":1,"customer_id":1,
                            "transaction_time":datetime.now(),"country":"IN","payment_method":"CRYPTO"}])
        self.assertIn("CRYPTO", detect_fraud(df,self.merchants).iloc[0]["fraud_reason"])

    def test_multiple_fraud_rules_trigger(self):
        df = pd.DataFrame([{"transaction_amount":200000,"merchant_id":1,"customer_id":1,
                            "transaction_time":datetime.now(),"country":"US","payment_method":"CRYPTO"}])
        reasons = detect_fraud(df,self.merchants).iloc[0]["fraud_reason"]
        self.assertTrue("HIGH_VALUE" in reasons and "CRYPTO" in reasons)