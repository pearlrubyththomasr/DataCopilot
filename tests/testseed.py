import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.db import execute_query

query = "SELECT * FROM BusinessPartner LIMIT 5"

result, error = execute_query(query)

if error:
    print("Error:", error)
else:
    print(result)