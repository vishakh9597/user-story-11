import pandas as pd
import logging

logger = logging.getLogger(__name__)

def load_merchants(path):
    try:
        df = pd.read_csv(path)
        logger.info(f"Loaded {len(df)} merchants")
        return df
    except Exception as e:
        logger.error(f"Error loading merchants: {e}")
        return pd.DataFrame()


def load_transactions(path):
    try:
        df = pd.read_csv(path)
        df["transaction_time"] = pd.to_datetime(df["transaction_time"], errors="coerce")
        logger.info(f"Loaded {len(df)} transactions")
        return df
    except Exception as e:
        logger.error(f"Error loading transactions: {e}")
        return pd.DataFrame()