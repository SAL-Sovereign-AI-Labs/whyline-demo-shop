OLD_TO_NEW = {"cust_id": "customer_id", "amt": "amount"}


def rename_columns(row):
    return {OLD_TO_NEW.get(k, k): v for k, v in row.items()}
