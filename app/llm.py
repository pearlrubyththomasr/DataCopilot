import requests

# -------------------------
# DEFAULT SCHEMA (fallback)
# -------------------------
DEFAULT_SCHEMA = """
BusinessPartner(BP_ID, BP_Name, Region, Industry)
SalesOrder(SO_ID, BP_ID, Order_Date, Total_Amount, Currency)
SalesOrderItem(Item_ID, SO_ID, Product_ID, Quantity, Net_Amount)
Product(Product_ID, Product_Name, Category, Price)
"""

# -------------------------
# CLEAN SQL
# -------------------------
def clean_sql(sql: str) -> str:
    return sql.replace("```sql", "").replace("```", "").strip()

# -------------------------
# GENERATE SQL
# -------------------------
def generate_sql(user_query: str, schema: str = None) -> str:
    schema = schema if schema else DEFAULT_SCHEMA

    prompt = f"""
You are an expert SQL generator.

STRICT RULES:
- Use ONLY SQLite syntax
- DO NOT use DATEADD, DATEDIFF, GETDATE
- Use DATE('now', '-X days/months')
- Use ONLY given schema
- Return ONLY SQL

Schema:
{schema}

User Query:
{user_query}

SQL:
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )

        return clean_sql(response.json()["response"])

    except Exception as e:
        print("LLM Error:", e)
        return "SELECT * FROM UserTable LIMIT 5;"

# -------------------------
# FIX SQL
# -------------------------
def fix_sql(user_query: str, bad_sql: str, error: str, schema: str = None) -> str:
    schema = schema if schema else DEFAULT_SCHEMA

    prompt = f"""
The SQL query failed.

Database: SQLite

Schema:
{schema}

User Query:
{user_query}

SQL:
{bad_sql}

Error:
{error}

Fix it. Return ONLY SQL.
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )

        return clean_sql(response.json()["response"])

    except:
        return bad_sql


def get_sql(user_query: str, schema: str = None) -> str:
    return generate_sql(user_query, schema)