import streamlit as st
# import os

# st.title("AI MoM Generator")

# uploaded_file = st.file_uploader(
#     "Upload meeting recording",
#     type=["mp4", "wav", "mp3"]
# )

# if uploaded_file:
#     os.makedirs("temp", exist_ok=True)
#     file_path = f"temp/{uploaded_file.name}"

#     with open(file_path, "wb") as f:
#         f.write(uploaded_file.read())

#     st.success("File uploaded successfully")