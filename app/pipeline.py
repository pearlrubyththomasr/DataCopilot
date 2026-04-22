import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.llm import get_sql, fix_sql
from app.db import execute_query
from app.validator import validate_sql
from app.explainability import explain_sql


def run_query_pipeline(user_query: str, schema: str = None):
    sql = get_sql(user_query, schema)
    print("\nGenerated SQL:\n", sql)

    is_valid, msg = validate_sql(sql)
    if not is_valid:
        return {"error": msg}

    result, error = execute_query(sql)

    if error:
        print("\nError detected:", error)

        fixed_sql = fix_sql(user_query, sql, error, schema)
        print("\nFixed SQL:\n", fixed_sql)

        result, error = execute_query(fixed_sql)

        if error:
            return {"error": error}

        return {
            "sql": fixed_sql,
            "result": result,
            "explanation": explain_sql(fixed_sql)
        }

    return {
        "sql": sql,
        "result": result,
        "explanation": explain_sql(sql)
    }