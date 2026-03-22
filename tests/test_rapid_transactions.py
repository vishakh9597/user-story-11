import unittest
import pandas as pd
from datetime import datetime, timedelta
from src.fraud_engine import detect_fraud

class TestRapid(unittest.TestCase):

    def setUp(self):
        self.merchants = pd.DataFrame({"merchant_id":[1],"country":["IN"]})

    def test_rapid_transactions_flagged(self):
        base = datetime.now()
        data = [{"transaction_amount":100,"merchant_id":1,"customer_id":1,
                 "transaction_time":base+timedelta(seconds=i*20),
                 "country":"IN","payment_method":"CARD"} for i in range(4)]
        df = pd.DataFrame(data)
        self.assertTrue(len(detect_fraud(df,self.merchants)
                            .query("fraud_reason.str.contains('RAPID')",engine='python'))>0)

    def test_transactions_outside_window_not_flagged(self):
        base = datetime.now()
        data = [{"transaction_amount":100,"merchant_id":1,"customer_id":1,
                 "transaction_time":base+timedelta(minutes=i*3),
                 "country":"IN","payment_method":"CARD"} for i in range(4)]
        df = pd.DataFrame(data)
        self.assertEqual(len(detect_fraud(df,self.merchants)
                             .query("fraud_reason.str.contains('RAPID')",engine='python')),0)