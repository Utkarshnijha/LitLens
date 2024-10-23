import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('books_of_the_decade.csv')

# Display column names
st.write("Column names:", df.columns.tolist())

# Optionally trim whitespace
df.columns = df.columns.str.strip()

# Convert Rating to numeric, coercing errors to NaN
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

# Check for NaN values and handle them
st.write("Number of NaN values in Rating:", df['Rating'].isna().sum())
df = df.dropna(subset=['Rating'])  # Optionally drop rows with NaN in Rating

# Display the top 10 books by rating
top_books = df.nlargest(10, 'Rating')
st.write("Top 10 Books by Rating:")
st.dataframe(top_books[['Book Name', 'Author', 'Rating']])

# Calculate average rating per author
average_rating = df.groupby('Author')['Rating'].mean().sort_values()

# Create a bar chart for average rating by author
plt.figure(figsize=(10, 5))
average_rating.plot(kind='barh')
plt.title('Average Rating by Author')
plt.xlabel('Average Rating')
plt.ylabel('Author')
st.pyplot(plt)

# Text input for book name search
book_name = st.text_input("Search for a book:", "")
if book_name:
    filtered_books = df[df['Book Name'].str.contains(book_name, case=False, na=False)]
    st.write("Search Results:")
    st.dataframe(filtered_books[['Book Name', 'Author', 'Rating']])
