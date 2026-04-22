import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.llm import get_sql

query = "Top 3 customers by revenue"

sql = get_sql(query)
print(sql)