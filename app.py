import streamlit as st
import pickle

# Load the model and vectorizer
with open('rf_model.pkl', 'rb') as model_file:
    rf_model = pickle.load(model_file)

with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    tfidf = pickle.load(vectorizer_file)

# Set custom CSS for background color and styling
st.markdown("""
    <style>
        body {
            background-color: #f0f4f8; /* Light grey-blue background */
        }
        .header {
            text-align: center;
            font-size: 36px;
            color: #2c3e50;  /* Dark blue color for the header */
        }
        .subheader {
            text-align: center;
            font-size: 18px;
            color: #7f8c8d;  /* Grey color for the subheader */
        }
        .content {
            font-size: 20px;
            color: #34495e;  /* Dark grey-blue text */
        }
        .result {
            font-size: 24px;
            font-weight: bold;
            color: #e74c3c;  /* Red color for result */
        }
    </style>
""", unsafe_allow_html=True)

# Dataset Introduction
st.markdown('<div class="header">Steam Review Sentiment Analysis</div>', unsafe_allow_html=True)


# Display Steam app image
st.image("steam.png", width=300)  # Ensure to place the image in the same directory as your app or provide a path to it

# Input Section
review = st.text_area("Enter your Steam review:")

# Button to trigger analysis
if st.button('Analyze'):
    if review:
        # Transform the review using the loaded Tfidf Vectorizer
        review_vectorized = tfidf.transform([review])
        
        # Predict sentiment using the trained model
        prediction = rf_model.predict(review_vectorized)

        # Display the result
        if prediction == 1:
            st.markdown('<div class="result" style="color: green;">Positive Review!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result" style="color: red;">Negative Review!</div>', unsafe_allow_html=True)
    else:
        st.write("Please enter a review to get a sentiment prediction.")

# Optional: Show more details about your app or developer information
st.write("""
This app is powered by a Random Forest model that has been trained to predict sentiment 
based on user reviews. The model has been trained using data from Steam reviews and processed 
using TF-IDF vectorization.
""")