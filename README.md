# CSV Data Visualizer

A Python application for uploading, processing, and visualizing CSV data with interactive charts.

## Components

### FastAPI Backend
- Processes uploaded CSV files
- Stores data in SQLite database
- Provides API endpoints for data retrieval

### Streamlit Frontend
- User-friendly interface for file uploads
- Interactive data visualization using Plotly
- Real-time data display

### SQLite Database
- Lightweight database for storing processed data
- Simple table structure for demonstration purposes

## Features

- CSV file upload and processing
- Data storage in SQLite database
- Interactive data visualization with Plotly
- RESTful API for data access
- Simple and intuitive user interface

## Installation

```bash
# Clone the repository
git clone https://github.com/angtooh39/csv-data-visualizer.git
cd csv-data-visualizer

# Install dependencies
pip install -r requirements.txt
```

## Running the Application

1. Start the FastAPI backend:
```bash
uvicorn main:app --reload
```

2. In a separate terminal, start the Streamlit frontend:
```bash
streamlit run streamlit_app.py
```

3. Open your browser and navigate to:
   - FastAPI docs: http://127.0.0.1:8000/docs
   - Streamlit app: http://localhost:8501

## API Endpoints

- `GET /`: Welcome message
- `POST /upload`: Upload and process CSV files
- `GET /data`: Retrieve all processed data

## CSV Format

The application expects CSV files with at least two columns named "column1" and "column2".

Example CSV format:
```
column1,column2
value1,10
value2,20
value3,30
```