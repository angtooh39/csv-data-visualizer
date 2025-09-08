from fastapi import FastAPI, UploadFile, File
import sqlite3
import pandas as pd

app = FastAPI()

# SQLite database setup
def init_db():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS processed_data (id INTEGER PRIMARY KEY, column1 TEXT, column2 TEXT)")
    conn.commit()
    conn.close()

init_db()

@app.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Read CSV file
    contents = await file.read()
    df = pd.read_csv(pd.compat.StringIO(contents.decode("utf-8")))

    # Process and store data
    for _, row in df.iterrows():
        cursor.execute("INSERT INTO processed_data (column1, column2) VALUES (?, ?)", (row["column1"], row["column2"]))

    conn.commit()
    conn.close()

    return {"message": "File processed and data stored successfully."}

@app.get("/data")
def get_data():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM processed_data")
    rows = cursor.fetchall()
    conn.close()

    return {"data": rows}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Library API"}