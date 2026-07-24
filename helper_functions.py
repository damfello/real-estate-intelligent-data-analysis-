# helper_functions.py
import pandas as pd
from sqlalchemy import text

# To query the SQL db
def run_query(query_string, engine):
    """Executes a SQL query and returns a pandas DataFrame."""
    return pd.read_sql(sql=text(query_string), con=engine)