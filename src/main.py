import logging
import os

from loader import load_merchants, load_transactions
from validator import validate_transactions
from fraud_engine import detect_fraud
from settlement_engine import generate_settlement
from reporter import save_outputs

os.makedirs("logs", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

logging.basicConfig(
    filename="logs/fraud_engine.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    logging.info("===== START =====")

    merchants = load_merchants("data/merchants.csv")
    transactions = load_transactions("data/transactions.csv")

    valid_txns = validate_transactions(transactions, merchants)
    processed = detect_fraud(valid_txns, merchants)
    settlement = generate_settlement(processed, merchants)

    save_outputs(processed, settlement)

    logging.info("===== END =====")
    print("✅ Done")


if __name__ == "__main__":
    main()