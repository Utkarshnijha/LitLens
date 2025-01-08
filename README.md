# Books of the Decade Project

**Description:** This project displays a list of notable books from the past decade, allows users to search for books by name, and shows data analyses (like average ratings) using Streamlit. Additionally, there's a placeholder for a Rasa chatbot service.

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

## Known Issues / Future Plans

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