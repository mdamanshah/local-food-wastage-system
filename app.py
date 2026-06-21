import streamlit as st
import pandas as pd

# Page Config
st.set_page_config(page_title="Local Food Wastage System", layout="wide")

# Load Data
providers = pd.read_csv("data/providers_data.csv")
receivers = pd.read_csv("data/receivers_data.csv")
food = pd.read_csv("data/food_listings_data.csv")
claims = pd.read_csv("data/claims_data.csv")

# Title
st.title("🍽️ Local Food Wastage Management System")

# Sidebar Navigation
page = st.sidebar.selectbox(
    "Navigation",
    ["Dashboard", "Providers", "Receivers", "Food Listings", "Claims"]
)

# =========================
# DASHBOARD
# =========================
if page == "Dashboard":

    st.header("Dashboard Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Providers", len(providers))
    col2.metric("Receivers", len(receivers))
    col3.metric("Food Listings", len(food))
    col4.metric("Claims", len(claims))

    st.markdown("---")

    st.subheader("Provider Type Distribution")
    st.bar_chart(providers["Type"].value_counts())

    st.subheader("Food Type Distribution")
    st.bar_chart(food["Food_Type"].value_counts())

    st.subheader("Meal Type Distribution")
    st.bar_chart(food["Meal_Type"].value_counts())

    st.subheader("Claims Status Distribution")
    st.bar_chart(claims["Status"].value_counts())

# =========================
# PROVIDERS
# =========================
elif page == "Providers":

    st.header("Providers Data")

    city = st.selectbox(
        "Select City",
        sorted(providers["City"].unique())
    )

    filtered_providers = providers[
        providers["City"] == city
    ]

    st.dataframe(filtered_providers)

# =========================
# RECEIVERS
# =========================
elif page == "Receivers":

    st.header("Receivers Data")

    city = st.selectbox(
        "Select Receiver City",
        sorted(receivers["City"].unique())
    )

    filtered_receivers = receivers[
        receivers["City"] == city
    ]

    st.dataframe(filtered_receivers)

# =========================
# FOOD LISTINGS
# =========================
elif page == "Food Listings":

    st.header("Food Listings")

    food_type = st.selectbox(
        "Select Food Type",
        sorted(food["Food_Type"].unique())
    )

    filtered_food = food[
        food["Food_Type"] == food_type
    ]

    st.dataframe(filtered_food)

# =========================
# CLAIMS
# =========================
elif page == "Claims":

    st.header("Claims Data")

    status = st.selectbox(
        "Select Claim Status",
        sorted(claims["Status"].unique())
    )

    filtered_claims = claims[
        claims["Status"] == status
    ]

    st.dataframe(filtered_claims)