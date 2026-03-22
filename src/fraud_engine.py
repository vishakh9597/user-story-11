import pandas as pd
from datetime import timedelta
import logging

logger = logging.getLogger(__name__)


def detect_fraud(df, merchants):
    if df.empty:
        return df

    df = df.copy()

    merchant_country = merchants.set_index("merchant_id")["country"].to_dict()

    df["fraud_flag"] = 0
    df["fraud_reason"] = ""
    df["transaction_status"] = "VALID"

    # Rule 1
    mask = df["transaction_amount"] > 100000
    df.loc[mask, "fraud_flag"] = 1
    df.loc[mask, "fraud_reason"] += "HIGH_VALUE_TRANSACTION,"

    # Rule 2
    mask = df["country"] != df["merchant_id"].map(merchant_country)
    df.loc[mask, "fraud_flag"] = 1
    df.loc[mask, "fraud_reason"] += "CROSS_BORDER_TRANSACTION,"

    # Rule 4
    mask = (df["payment_method"] == "CRYPTO") & (df["transaction_amount"] > 50000)
    df.loc[mask, "fraud_flag"] = 1
    df.loc[mask, "fraud_reason"] += "CRYPTO_HIGH_VALUE,"

    # Rule 3 (Rapid)
    df = df.sort_values(by=["customer_id", "transaction_time"])

    for cust_id, group in df.groupby("customer_id"):
        times = group["transaction_time"].tolist()

        for i in range(len(times)):
            count = 1
            for j in range(i + 1, len(times)):
                if times[j] - times[i] <= timedelta(minutes=2):
                    count += 1
                else:
                    break

            if count > 3:
                idx = group.index[i:j+1]
                df.loc[idx, "fraud_flag"] = 1
                df.loc[idx, "fraud_reason"] += "RAPID_TRANSACTIONS,"

    df["fraud_reason"] = df["fraud_reason"].str.strip(",")
    df.loc[df["fraud_flag"] == 1, "transaction_status"] = "SUSPICIOUS"

    logger.info("Fraud detection done")
    return df