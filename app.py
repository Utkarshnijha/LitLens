import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import random
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
# Load dataset
df = pd.read_csv("books_of_the_decade.csv")

# Debug: Inspect the dataset
st.write("Dataset Overview:")
st.write(df.head())  # Display the first few rows of the dataset
st.write("Dataset Info:")
st.write(df.info())  # Show data types and non-null counts
st.write("Dataset Description:")
st.write(df.describe())  # Display statistics for numeric columns
@st.cache_data
def load_and_preprocess_data():
    data = pd.read_csv('books_of_the_decade.csv')  # Load the dataset

    
    # Drop unnecessary columns
    data = data.drop(['Index'], axis=1, errors='ignore')
    
    # Convert 'Rating' to numeric, coercing errors to NaN
    data['Rating'] = pd.to_numeric(data['Rating'].str.replace(',', ''), errors='coerce')
    
    # Handle missing values - drop rows with NaN in 'Rating'
    data.dropna(subset=['Rating'], inplace=True)
    
    return data

# Streamlit app title
st.title("Welcome to My Multipage App")
st.write("Use the sidebar to navigate between pages.")

# Load and preprocess data
data = load_and_preprocess_data()

# Display error if data is empty
if data.empty:
    st.error("The dataset is empty. Please check the file content.")
else:
    # Clean 'Number of Votes' and 'Score' columns
    for col in ['Number of Votes', 'Score']:
        # Replace commas only if the column is of string type
        if data[col].dtype == 'object':
            data[col] = data[col].str.replace(',', '', regex=True)

        # Convert to numeric and coerce errors to NaN
        data[col] = pd.to_numeric(data[col], errors='coerce')

    # Drop rows with NaN values after conversion
    data.dropna(subset=['Number of Votes', 'Score'], inplace=True)

    # Display the top 10 books by rating
    top_books = data.nlargest(10, 'Rating')
    st.write("Top 10 Books by Rating:")
    st.dataframe(top_books[['Book Name', 'Author', 'Rating']])

    # Calculate average rating per author
    average_rating = data.groupby('Author')['Rating'].mean().sort_values()

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
        filtered_books = data[data['Book Name'].str.contains(book_name, case=False, na=False)]
        st.write("Search Results:")
        st.dataframe(filtered_books[['Book Name', 'Author', 'Rating']])

    # Generate fake data
    def generate_fake_data(num_entries):
        fake_data = []
        for _ in range(num_entries):
            book_name = f"Fake Book {_ + 1}"
            author = f"Author {_ + 1}"
            rating = random.uniform(1.0, 5.0)  # Random rating between 1.0 and 5.0
            num_votes = random.randint(0, 1000)  # Random votes between 0 and 1000
            score = round(rating * num_votes, 2)  # Example score calculation

            fake_data.append({
                'Book Name': book_name,
                'Author': author,
                'Rating': round(rating, 1),
                'Number of Votes': num_votes,
                'Score': score
            })
        
        return pd.DataFrame(fake_data)

    # Generate fake data
    existing_data_size = len(data)
    min_fake_entries = int(existing_data_size * 0.25)  # 25%
    max_fake_entries = int(existing_data_size * 0.5)    # 50%
    num_fake_entries = random.randint(min_fake_entries, max_fake_entries)

    fake_books_df = generate_fake_data(num_fake_entries)  # Generate fake entries

    # Combine the datasets
    combined_data = pd.concat([data, fake_books_df], ignore_index=True)
    # Select features and target variable
    X = df[['Rating', 'Number of Votes']]  # Replace with actual feature columns
    y = df['Score']  # Replace with the target column

    # Debug: Inspect feature variables
    st.write("Feature Variables (X):")
    st.write(X.head())
    st.write("Target Variable (y):")
    st.write(y.head())
    
    # Define feature columns and target variable for model training
    X = combined_data[['Number of Votes', 'Score']]  # Features used for prediction
    y = combined_data['Rating']  # Target variable

    # Split data into training, validation, and test sets
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Debug: Inspect training and test data
    st.write("Training Features (X_train):")
    st.write(X_train.head())
    st.write("Training Target (y_train):")
    st.write(y_train.head())
    st.write("Test Features (X_test):")
    st.write(X_test.head())
    st.write("Test Target (y_test):")
    st.write(y_test.head())

    # Train the model
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X_train, y_train)
    # Initialize and train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    # Debug: Display model coefficients
    st.write("Model Coefficients:")
    st.write(model.coef_)
    st.write("Model Intercept:")
    st.write(model.intercept_)

    # Evaluate the model on validation data
    y_val_pred = model.predict(X_val)
    
    # Debug: Display inputs and predictions for first few rows
    st.write("Sample Test Inputs (X_val):")
    st.write(X_val[:10])  # Show first 10 rows of test inputs
    st.write("Sample Predicted Values:")
    st.write(y_val_pred[:10])  # Show first 10 predictions
    st.write("Sample Actual Values:")
    st.write(y_test[:10])  # Show first 10 actual values

    # Debug: Display all test inputs and predictions (optional)
    st.write("Full Test Features:")
    st.write(X_val)
    st.write("Full Predicted Values:")
    st.write(y_val_pred)


    # Calculate the metrics
    val_mse = mean_squared_error(y_val, y_val_pred)
    val_mae = mean_absolute_error(y_val, y_val_pred)
    val_r2 = r2_score(y_val, y_val_pred)

    # Display Validation Results
    st.subheader("Model Validation Results")
    st.write("Mean Squared Error on Validation Set:", val_mse)
    st.write("Mean Absolute Error (MAE) on Validation Set:", val_mae)
    st.write("R-squared (R²) on Validation Set:", val_r2)

    # Plot predictions vs actual values
    plt.figure(figsize=(10, 5))
    plt.scatter(y_val, y_val_pred, alpha=0.5)
    plt.plot([y_val.min(), y_val.max()], [y_val.min(), y_val.max()], 'r--')  # Identity line
    plt.xlabel('Actual Ratings')
    plt.ylabel('Predicted Ratings')
    plt.title('Actual vs Predicted Ratings')
    plt.xlim([1, 5])  # Assuming ratings are from 1 to 5
    plt.ylim([1, 5])
    st.pyplot(plt)

    # Display the combined data in Streamlit
    st.title("Combined Books Data (Real + Fake)")
    st.write(combined_data)

    # Calculate and Display Statistics
    statistics = combined_data.describe()
    st.subheader("Descriptive Statistics of Combined Data")
    st.write(statistics)
    # Check for missing values
    st.write("Missing Values in Dataset:")
    st.write(df.isnull().sum())
    df.fillna(0, inplace=True)