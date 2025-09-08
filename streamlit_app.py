import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.title("CSV File Uploader and Data Visualizer")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    # Display uploaded file
    st.write("Uploaded File:")
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    # Send file to FastAPI backend
    with st.spinner("Processing file..."):
        response = requests.post("http://127.0.0.1:8000/upload", files={"file": uploaded_file.getvalue()})
        if response.status_code == 200:
            st.success("File processed and data stored successfully.")
        else:
            st.error("Failed to process file.")

    # Fetch processed data
    response = requests.get("http://127.0.0.1:8000/data")
    if response.status_code == 200:
        data = response.json()["data"]
        processed_df = pd.DataFrame(data, columns=["ID", "Column1", "Column2"])
        st.write("Processed Data:")
        st.dataframe(processed_df)

        # Plotly visualization
        st.write("Data Visualization:")
        fig = px.bar(processed_df, x="Column1", y="Column2", title="Bar Chart of Processed Data")
        st.plotly_chart(fig)
    else:
        st.error("Failed to fetch processed data.")