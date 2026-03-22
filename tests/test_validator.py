import unittest
import pandas as pd
from src.validator import validate_transactions

class TestValidator(unittest.TestCase):

    def test_invalid_merchant_rejected(self):
        merchants = pd.DataFrame({"merchant_id":[1],"status":["ACTIVE"]})
        txns = pd.DataFrame([{"merchant_id":2,"transaction_amount":100,"transaction_time":"2025"}])
        self.assertEqual(len(validate_transactions(txns, merchants)), 0)

    def test_blocked_merchant_rejected(self):
        merchants = pd.DataFrame({"merchant_id":[1],"status":["BLOCKED"]})
        txns = pd.DataFrame([{"merchant_id":1,"transaction_amount":100,"transaction_time":"2025"}])
        self.assertEqual(len(validate_transactions(txns, merchants)), 0)

    def test_negative_amount_rejected(self):
        merchants = pd.DataFrame({"merchant_id":[1],"status":["ACTIVE"]})
        txns = pd.DataFrame([{"merchant_id":1,"transaction_amount":-1,"transaction_time":"2025"}])
        self.assertEqual(len(validate_transactions(txns, merchants)), 0)

    def test_invalid_timestamp_handling(self):
        merchants = pd.DataFrame({"merchant_id":[1],"status":["ACTIVE"]})
        txns = pd.DataFrame([{"merchant_id":1,"transaction_amount":100,"transaction_time":"invalid"}])
        txns["transaction_time"]=pd.to_datetime(txns["transaction_time"],errors="coerce")
        self.assertEqual(len(validate_transactions(txns, merchants)), 0)