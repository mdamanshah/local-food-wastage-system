import pandas as pd

providers = pd.read_csv("data/providers_data.csv")
receivers = pd.read_csv("data/receivers_data.csv")
food = pd.read_csv("data/food_listings_data.csv")
claims = pd.read_csv("data/claims_data.csv")

print("Providers Shape:", providers.shape)
print("Receivers Shape:", receivers.shape)
print("Food Shape:", food.shape)
print("Claims Shape:", claims.shape)

print("\nProviders Sample:")
print(providers.head())