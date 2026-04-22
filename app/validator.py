def validate_sql(sql: str) -> (bool, str):
    forbidden = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER"]

    for word in forbidden:
        if word in sql.upper():
            return False, f"Forbidden keyword detected: {word}"

    return True, "" 