import streamlit as st
import pandas as pd

# Load data with caching
@st.cache_data
def load_data():
    return pd.read_csv("books_of_the_decade.csv")

df = load_data()

st.title("Book Search")
st.write("Find your next favorite book based on genre or rating!")

# Genre filter
genre = st.selectbox("Select a genre:", sorted(df["Genre"].unique()))
filtered_books = df[df["Genre"] == genre]

# Rating filter
min_rating = st.slider("Minimum Rating", 0.0, 5.0, 3.5)
filtered_books = filtered_books[filtered_books["Rating"] >= min_rating]

# Display filtered books
if not filtered_books.empty:
    st.write(f"Books in the genre '{genre}' with rating >= {min_rating}:")
    st.dataframe(filtered_books[["Title", "Author", "Rating"]])
else:
    st.write("No books found. Try adjusting the filters!")
