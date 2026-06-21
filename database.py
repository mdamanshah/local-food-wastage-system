from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "postgresql+psycopg2://postgres:VhxAman786@localhost:5432/food_waste_db"
)

try:
    conn = engine.connect()
    print("Connected Successfully!")

    providers = pd.read_csv("data/providers_data.csv")
    receivers = pd.read_csv("data/receivers_data.csv")
    food = pd.read_csv("data/food_listings_data.csv")
    claims = pd.read_csv("data/claims_data.csv")

    providers.to_sql("providers", engine, if_exists="replace", index=False)
    receivers.to_sql("receivers", engine, if_exists="replace", index=False)
    food.to_sql("food_listings", engine, if_exists="replace", index=False)
    claims.to_sql("claims", engine, if_exists="replace", index=False)

    print("All data imported successfully!")

except Exception as e:
    print("ERROR:")
    print(e)
