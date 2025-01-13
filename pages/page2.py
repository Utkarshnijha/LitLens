import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data with caching
@st.cache_data
def load_data():
    return pd.read_csv("books_of_the_decade.csv")

df = load_data()

# Ensure 'Rating' is numeric
df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")

st.title("Data Visualizations")
st.write("Explore insights from the best books of the decade.")

# Example: Average Rating by Author
avg_rating = df.groupby("Author")["Rating"].mean().sort_values(ascending=False).head(10)
st.subheader("Top 10 Authors by Average Rating")
fig, ax = plt.subplots()
avg_rating.plot(kind="bar", ax=ax)
st.pyplot(fig)

# Example: Distribution of Ratings
st.subheader("Distribution of Book Ratings")
fig, ax = plt.subplots()
df["Rating"].plot(kind="hist", bins=20, ax=ax, title="Book Ratings Distribution")
st.pyplot(fig)
