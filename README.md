# Sentiment Analysis on Steam Game Reviews

### Overview:
This project performs sentiment analysis on Steam game reviews using Natural Language Processing (NLP) techniques. The project identifies whether sentiments are positive or negative by analyzing user reviews. The results are showcased using a Streamlit web application, which provides an interactive real-time platform to explore and analyze sentiment data.

### **Sentiment Analysis Results**
After uploading a dataset or entering text, the app provides visual feedback:



### Dataset:

Steam Reviews & Games Dataset
Source: Kaggle.

### Description:

The dataset includes game reviews labeled as positive (1) or negative (0).
It provides structured data suitable for sentiment classification and machine learning projects.

### Columns:
id: Unique identifier for the review.
app_id: Game identifier on Steam.
content: The review text.
author_id: Identifier of the review's author.
is_positive: Sentiment label (1 for positive, 0 for negative).

### Potential Use Cases:
Sentiment classification (positive vs. negative).


## **Features**
### **Key Project Components**
1. **Data Preprocessing**:
   - Cleaning and tokenizing text reviews.
   - Removing noise like special characters, stopwords, and redundant text.
   - Applying lemmatization for consistency.
2. **Sentiment Classification**:
   - Using logistic regression, Svc, Random forest, Lstm.
   - Reviews are classified into two categories: **positive** or **negative**.
3. **Streamlit Web Application**:
   - Interactive dashboard to:
     - Enter custom text for sentiment analysis.
4. **Outlier Retention**:
   - Outliers were intentionally kept to capture extreme positive and negative reviews for a more realistic sentiment analysis.

---

## **Tech Stack**
- **Programming Language**: Python
- **Libraries Used**:
  - **Data Processing**: `pandas`, `numpy`
  - **NLP**: `nltk`.
  - **Visualization**: `matplotlib`.
  - **Web App**: `streamlit`

---

## **How It Works**
1. **Load Dataset**:
   - Steam reviews are loaded from `steam_data.csv`.
2. **Data Cleaning**:
   - The text data is preprocessed by removing unnecessary characters, stopwords, and redundant information.
3. **Sentiment Scoring**:
   - Reviews are analyzed to determine whether the sentiment is positive or negative.
4. **Interactive App**:
   - Users can input custom text for analysis.
5. **Outlier Handling**:
   - Outliers (extreme sentiment values) were retained to maintain data integrity and reflect real-world variability in user feedback.

---

### Reason for Retaining Outliers

Outliers in sentiment scores were retained to:

1. Preserve extreme opinions, such as highly positive or negative reviews, which provide valuable insights.
2. Ensure the real-world variability of user reviews is captured.
3. Improve the model’s generalization ability by learning from the entire spectrum of sentiments.

### Future Work

1. Add support for neutral sentiment classification.
2. Extend analysis to cover multilingual reviews.
3. Use advanced NLP models like BERT or GPT for improved accuracy.
4. Add trend analysis for reviews grouped by app_id (game identifier).




