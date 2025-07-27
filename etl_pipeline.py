import json
import pandas as pd
from sqlalchemy import create_engine

# Load simulated events
with open("moderation_events.json") as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Apply data cleaning and transformations
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["is_accurate"] = df["review_accuracy"] > 0.85
df["cost_bucket"] = pd.cut(df["review_cost"], bins=[0, 2, 4, 5], labels=["Low", "Medium", "High"])

# Load into Redshift (via SQLAlchemy mock)
engine = create_engine("postgresql://username:password@redshift-cluster-endpoint/dbname")

df.to_sql("moderation_reviews", con=engine, if_exists='replace', index=False)

print("ETL pipeline executed successfully. Data loaded into Redshift.")
