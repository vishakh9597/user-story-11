import pandas as pd
import logging

logger = logging.getLogger(__name__)


def validate_transactions(transactions, merchants):
    if transactions.empty or merchants.empty:
        return pd.DataFrame()

    active_merchants = merchants[merchants["status"] == "ACTIVE"]["merchant_id"]

    valid_rows = []

    for _, row in transactions.iterrows():

        if row["merchant_id"] not in merchants["merchant_id"].values:
            logger.error(f"Unknown merchant: {row['merchant_id']}")
            continue

        if row["merchant_id"] not in active_merchants.values:
            logger.error(f"Blocked merchant: {row['merchant_id']}")
            continue

        if row["transaction_amount"] <= 0:
            logger.error(f"Invalid amount: {row['transaction_id']}")
            continue

        if pd.isna(row["transaction_time"]):
            logger.error(f"Invalid timestamp: {row['transaction_id']}")
            continue

        valid_rows.append(row)

    logger.info(f"Valid transactions: {len(valid_rows)}")
    return pd.DataFrame(valid_rows)