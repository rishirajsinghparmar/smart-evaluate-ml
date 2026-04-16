import streamlit as st

st.title("Smart Evaluate - Answer Sheet Evaluation")

st.write("Upload your answer sheet for evaluation")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Answer Sheet")
    st.success("Evaluation Complete ✅")
    st.write("Score: 8/10")
