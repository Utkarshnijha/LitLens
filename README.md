
# Books of the Decade 
---------------------
Name: - Utkarshni

Matriculation: 22306093

**Project was done by me alone**
---------------------------------

Title: Books of the Decade

Link to MyGit Repository is: https://mygit.th-deg.de/ar08397/LitLens.git

Link of MyGit Wiki is: https://mygit.th-deg.de/ar08397/LitLens/-/wikis/pages
  

**Description:** LitLens is a data-driven web application designed to recommend and analyze books from the past decade. It combines modern technologies such as Streamlit and Rasa to provide users with an interactive chatbot, detailed book statistics, and tailored recommendations. The project aims to enhance the experience of book lovers by providing insightful data visualizations, intuitive navigation, and personalized suggestions.


### Key Features
-----------------
- Multi-page Streamlit Web App

- Book recommendation system based on ratings

- User-friendly interface with input widgets for dynamic interactions

- Visualizations and statistics of book data

- Chatbot integration for user queries



**Data Description**
---------------------
The project uses a dataset from Kaggle titled 'Best Books of the Decade: 2020s'. The data includes columns such as:

- Book Name: Title of the book

- Author: Author of the book

- Rating: Average rating of the book

- Number of Votes: Number of votes the book has received

- Score: Overall score of the book

The data is analyzed in the app using Pandas, with visualizations of basic statistics like min/max, median, and correlations.


**Machine Learning Models**
----------------------------
Two machine learning models were applied to predict book ratings:

**Linear Regression**

**Decision Tree Regressor**

The models are evaluated in the app, and the best performing model is discussed in the Wiki.

**Chatbot Integration**
-----------------------
The project includes a Rasa chatbot to handle the following use cases:

- Browsing Popular Books

- Recommending Books Based on Ratings

The system persona for the chatbot is documented in the Wiki, along with sample dialogues and a high-level dialog flow.


## Installation
----------------
### Prerequisites
- **Python Version**: 3.10.x
- **Rasa Version**: 3.6.20
- **Streamlit Version**: 1.25.0
- **scikit-learn Version**: 1.3.1
- **Docker Version**: 24.x (for containerized deployment)



## Quick Start

1. **Clone** this repository:

   ```bash
   git clone https://mygit.th-deg.de/uu18093/LitLens.git
   cd LitLens
   ```

2. **Build and run** with Docker Compose:

   ```bash
   docker-compose up --build -d
   ```

   - After the containers start, open [http://localhost:8501](http://localhost:8501) in your browser.
   - The Rasa container listens on [http://localhost:5005](http://localhost:5005).

3. **Usage**:
   - On the **Streamlit** app main page, you can see top-rated books, average rating by author, and a search bar to find specific books.
   - The `pages/4_Chatbot.py` is a placeholder to integrate with a Rasa chatbot. Currently, it displays a “Chatbot integration coming soon!” message.

## Directory Structure

```
.
├── Dockerfile               # Builds the Streamlit-based book_app container
├── docker-compose.yml       # Orchestrates book_app and rasa_server containers
├── app.py                   # Main Streamlit app
├── requirements.txt         # Python dependencies
├── books_of_the_decade.csv  # CSV data with book info
├── pages/
│   └── 4_Chatbot.py         # Placeholder chatbot page
└── README.md                # This file
```



**Data**
---------
Source: The dataset "Best Books of the Decade: 2020s" [https://www.kaggle.com/datasets/valakhorasani/best-books-of-the-decade-2020s] was sourced from Kaggle.
Handling Outliers: Identified and removed data entries with extreme or unrealistic ratings and votes.
Fake Data: Added 25-50% synthetic entries for enhanced visualization and testing, generated using Python's random and faker libraries.


**Basic Usage**
----------------
Open the Streamlit app in your browser at http://localhost:8501
Navigate through the tabs to:

--> View statistics and visualizations for top-rated books.

--> Search for books based on title or author.

--> Interact with the chatbot on the "Chatbot" page.


## Known Issues / Future Plans
------------------------------

- The CSV data might need additional cleanup (duplicates, missing columns).
- The Rasa container is started but not integrated into the Streamlit app.
- The `Chatbot` page is only a placeholder.

<!--
## TODO (Commented Out for Now)

1. **Integrate Rasa**: Create a REST channel or a direct socket channel for communication between the Streamlit UI and the Rasa server.
2. **Add More Data Viz**: For authors with multiple books, show charts/trends.
3. **Handle Large CSV**: Possibly switch to a database if the CSV grows too large.
4. **Authentication**: If needed, secure the app behind login.

### Explanation
- We give quick commands for running Docker Compose.
- We show how to use it.
- We show the basic structure.
- At the bottom, there is a **commented-out** TODO section.  

---

## How to Run

From the **project root** directory:
1. `docker-compose build`
2. `docker-compose up -d`
3. Visit **[http://localhost:8501](http://localhost:8501)** in your browser.  

The Rasa container will be running at **[http://localhost:5005](http://localhost:5005)**. Currently, the Streamlit app is not calling Rasa, but you can expand the integration in your `pages/4_Chatbot.py` or a dedicated Python script.

---

### **Enjoy your new, streamlined, Dockerized “Books of the Decade” project!**

-->
**Acknowledgements**
--------------------
The Kaggle dataset was used for the book data.
Special thanks to the Rasa and Streamlit communities for providing powerful tools for the project.