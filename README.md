# UserStory11
This is Python based Payment Transaction Fraud Detection &amp; Settlement Engine Project where it processes transaction data, applies fraud rules, and generates transaction settlement outputs.

# Payment Transaction Fraud Detection & Settlement Engine

## Overview

This project implements a Python-based fraud detection and settlement engine designed for fintech systems that process large volumes of daily transactions. The system validates transaction data, detects suspicious activities using rule-based logic, and generates settlement reports for merchants. It ensures that only valid transactions are considered for settlement while identifying potentially fraudulent ones before processing.

## Key Features

* Load merchant and transaction data from CSV files
* Validate transactions using business rules
* Detect fraud using multiple rule-based checks
* Identify rapid transactions using time-window logic
* Compute settlement amounts per merchant
* Generate structured output reports (CSV & JSON)
* Log errors and invalid records
* Unit testing using Python `unittest`

## Business Logic

### Transaction Validation

Transactions are rejected if:

* Merchant ID does not exist
* Merchant status is **BLOCKED**
* Transaction amount ≤ 0
* Invalid timestamp format

### Fraud Detection Rules

A transaction is flagged as **SUSPICIOUS** if any of the following apply:

* **High Value Transaction** → Amount > 100000
* **Cross Border Transaction** → Transaction country ≠ Merchant country
* **Rapid Transactions** → More than 3 transactions within 2 minutes (same customer)
* **Crypto High Value** → Payment method = CRYPTO and amount > 50000

### Settlement Rules

* Only **VALID** transactions are included
* Settlement amount = sum of valid transactions per merchant

## Project Structure

```
project/
│
├── data/
│   ├── merchants.csv
│   ├── transactions.csv
│
├── src/
│   ├── __init__.py
│   ├── loader.py
│   ├── validator.py
│   ├── fraud_engine.py
│   ├── settlement_engine.py
│   ├── reporter.py
│   └── main.py
│
├── tests/
│   ├── test_validator.py
│   ├── test_fraud_engine.py
│   ├── test_settlement_engine.py
│
├── logs/
│   └── fraud_engine.log
│
├── outputs/
│   ├── processed_transactions.csv
│   ├── merchant_settlement_report.csv
│   └── fraud_summary.json
```

## How to Run

### Run the application

```bash
python3 src/main.py
```

### Run unit tests

```bash
python3 -m unittest discover tests
```

## Output Files

* **processed_transactions.csv** → Transaction-level data with fraud flags
* **merchant_settlement_report.csv** → Merchant-level settlement summary
* **fraud_summary.json** → Aggregated fraud metrics

## Assumptions

* Input files follow the required schema
* Timestamp format: `YYYY-MM-DD HH:MM:SS`
* Merchant IDs are case-sensitive
* Fraud rules are independent and may trigger simultaneously

## Edge Cases Handled

* Invalid timestamps
* Negative or zero transaction amounts
* Unknown merchants
* Blocked merchants
* Rapid transaction bursts

## Testing

The project includes unit tests using the `unittest` framework, covering:

* Transaction validation
* Fraud detection rules
* Settlement calculations

This ensures correctness, reliability, and maintainability of the system.

## Skills Demonstrated

* Python modular architecture
* Data validation and processing
* Rule-based fraud detection systems
* Time-window algorithms
* Logging and error handling
* Unit testing and debugging

## Future Improvements

* Integration with real-time streaming systems
* Machine learning-based fraud detection
* API-based service deployment
* Dashboard for fraud analytics# user-story-11
