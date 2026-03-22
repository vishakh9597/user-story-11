import pandas as pd
import logging

logger = logging.getLogger(__name__)

def generate_settlement(df, merchants):
    result = []

    for merchant_id, group in df.groupby("merchant_id"):
        merchant_info = merchants[merchants["merchant_id"] == merchant_id].iloc[0]

        total = len(group)
        valid = len(group[group["transaction_status"] == "VALID"])
        fraud = len(group[group["transaction_status"] == "SUSPICIOUS"])

        settlement = group[group["transaction_status"] == "VALID"]["transaction_amount"].sum()

        result.append({
            "merchant_id": merchant_id,
            "merchant_name": merchant_info["merchant_name"],
            "total_transactions": total,
            "valid_transactions": valid,
            "fraud_transactions": fraud,
            "settlement_amount": settlement
        })

    logger.info("Settlement generated")
    return pd.DataFrame(result)