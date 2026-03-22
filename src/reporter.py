import json

def save_outputs(df, settlement_df):
    df.to_csv("outputs/processed_transactions.csv", index=False)
    settlement_df.to_csv("outputs/merchant_settlement_report.csv", index=False)

    summary = {
        "total_transactions": len(df),
        "valid_transactions": len(df[df["transaction_status"] == "VALID"]),
        "fraud_transactions": len(df[df["transaction_status"] == "SUSPICIOUS"]),
        "high_value_frauds": len(df[df["fraud_reason"].str.contains("HIGH_VALUE", na=False)]),
        "cross_border_frauds": len(df[df["fraud_reason"].str.contains("CROSS_BORDER", na=False)]),
        "rapid_transaction_frauds": len(df[df["fraud_reason"].str.contains("RAPID", na=False)])
    }

    with open("outputs/fraud_summary.json", "w") as f:
        json.dump(summary, f, indent=4)