import streamlit as st
import joblib
import re
from scipy.sparse import hstack

# Load saved models
tfidf = joblib.load("tfidf.pkl")
classifier = joblib.load("classifier.pkl")
regressor = joblib.load("regressor.pkl")

keywords = ["graph", "dp", "dynamic programming", "recursion", "tree", "greedy"]
math_symbols = "+-*/=<>^"

def clean_text(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text

st.title("Programming Problem Difficulty Predictor")
st.write("Paste the problem details and click Predict.")

problem_desc = st.text_area("Problem Description")
input_desc = st.text_area("Input Description")
output_desc = st.text_area("Output Description")

if st.button("Predict Difficulty"):
    combined_text = clean_text(problem_desc + " " + input_desc + " " + output_desc)

    X_tfidf = tfidf.transform([combined_text])

    extra_features = [[
        len(combined_text),
        sum(combined_text.count(s) for s in math_symbols),
        *[combined_text.count(k) for k in keywords]
    ]]

    X_final = hstack([X_tfidf, extra_features])

    predicted_class = classifier.predict(X_final)[0]
    predicted_score = regressor.predict(X_final)[0]

    st.success(f"Predicted Difficulty Class: {predicted_class}")
    st.success(f"Predicted Difficulty Score: {round(predicted_score, 2)}")

