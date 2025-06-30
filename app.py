import streamlit as st
import helper
import pickle
import joblib

# Load the ML classification model
model = joblib.load('model11.pkl')

# Load the Word2Vec model (required by helper.query_point_creator)
word2vec_model = pickle.load(open('word2vec.pkl', 'rb'))

st.header("Duplicate Question Pairs Detection")

q1 = st.text_input("Enter Question 1")
q2 = st.text_input("Enter Question 2")

if st.button("Find"):
    # Pass the correct word2vec_model to query_point_creator
    query = helper.query_point_creator(q1, q2, word2vec_model)

    # Predict using your trained ML model
    result = model.predict(query)[0]

    if result:
        st.success("✅ The questions are duplicates.")
    else:
        st.error("❌ The questions are not duplicates.")
