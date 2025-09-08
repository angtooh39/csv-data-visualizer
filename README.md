# CSV Data Visualizer

A Python application that uses Streamlit for frontend, FastAPI for backend, and SQLite for database to process and visualize CSV data.

## Components

- **Frontend**: Streamlit application for uploading CSV files and displaying visualizations
- **Backend**: FastAPI server for processing data and database operations
- **Database**: SQLite for storing processed data

## Features

- Upload CSV files through a user-friendly interface
- Process data on the backend
- Store processed data in a SQLite database
- Display interactive data visualizations using Plotly

## How to Run

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Start the FastAPI backend:
   ```
   uvicorn main:app --reload
   ```

3. Start the Streamlit frontend:
   ```
   streamlit run streamlit_app.py
   ```

4. Open your browser and navigate to the Streamlit URL (typically http://localhost:8501)
