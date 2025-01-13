import streamlit as st
import pandas as pd

# Load data with caching
@st.cache_data
def load_data():
    return pd.read_csv("books_of_the_decade.csv")

df = load_data()

# Convert Rating column to numeric (if it's not already)
df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")

# Drop rows where Rating is NaN
df = df.dropna(subset=["Rating"])

st.title("Book Search")
st.write("Find your next favorite book based on rating!")

# Example: Select a book name from the 'Book Name' column
book_name = st.selectbox("Select a book:", sorted(df["Book Name"].unique()))

# Rating filter
min_rating = st.slider("Minimum Rating", 0.0, 5.0, 3.5)

# Filter the books based on the selected book and rating
filtered_books = df[(df["Book Name"] == book_name) & (df["Rating"] >= min_rating)]

# Display filtered books
if not filtered_books.empty:
    st.write(f"Books with rating >= {min_rating}:")
    st.dataframe(filtered_books[["Book Name", "Author", "Rating"]])
else:
    st.write("No books found. Try adjusting the filters!")
