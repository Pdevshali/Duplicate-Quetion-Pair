import streamlit as st
import helper
import pickle

# model = pickle.load(open('model.pkl', 'rb'))
import joblib
model = joblib.load('model_compressed.pkl')
# Add a comment
# "trigger rebuild" 


st.header("Duplicate Question pairs Detection")

q1 = st.text_input("Enter Question 1")
q2 = st.text_input("Enter Question 2")


if st.button("Find"):
    query = helper.query_point_creator(q1, q2)
    result = model.predict(query)[0]    # ✅ Correct

    if result:
        st.header("The questions are duplicates.")
    else:
        st.header("The questions are not duplicates.")