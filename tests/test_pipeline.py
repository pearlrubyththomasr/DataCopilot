import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.pipeline import run_query_pipeline

query = "Show top 3 customers by revenue"

output = run_query_pipeline(query)

print("\nFinal Output:\n", output)