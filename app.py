
import streamlit as st
import joblib

# Load model and TF-IDF
model = joblib.load("model.pkl")
tfidf = joblib.load("tfidf.pkl")

st.title("📱 SMS Spam Classifier")

message = st.text_area("Enter your SMS message:")

if st.button("Predict"):

    if message.strip() == "":
        st.warning("Please enter a message.")
    else:
        message_tfidf = tfidf.transform([message])

        prediction = model.predict(message_tfidf)

        if prediction[0] == 1:
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Ham Message")
