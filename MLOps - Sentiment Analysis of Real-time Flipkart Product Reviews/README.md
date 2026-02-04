# Sentiment Analysis of Real-time Flipkart Product Reviews

An end-to-end **MLOps project** that performs sentiment analysis on real Flipkart product reviews and deploys a trained model using **Streamlit Community Cloud**. The application classifies customer reviews as **Positive** or **Negative** and provides insights into customer satisfaction and pain points.

### App Link: https://sentiment-analysis-flipkart-reviews.streamlit.app

---

## Project Overview

**Objective**  
To analyze real-time Flipkart product reviews and:
- Classify reviews into **Positive** or **Negative** sentiment
- Understand common pain points from negative reviews
- Deploy a scalable, production-ready ML system using MLOps best practices

**Product Analyzed**  
  *YONEX MAVIS 350 Nylon Shuttle* (Flipkart)

---

## Dataset Description

- **Source**: Real-time scraped Flipkart reviews
- **File**: `data.csv`
- **Total Reviews**: 8,518

**Key Features**
- Reviewer Name  
- Rating  
- Review Title  
- Review Text  
- Place of Review  
- Date of Review  
- Up Votes / Down Votes  

---

## Data Preprocessing

- Text cleaning (lowercasing, special character & punctuation removal)
- Stopword removal
- Lemmatization
- Handling missing and noisy data
- Label creation using ratings (Positive / Negative)

---

## Feature Engineering

Multiple text representation techniques were explored:
- Bag of Words (BoW)
- TF-IDF (final selected approach)
- (Design supports future extension to Word2Vec / BERT)

---

## Model Training & Evaluation

- Multiple ML models trained and compared
- Best model selected using **F1-Score**
- Model artifacts and metadata saved for reproducibility

**Evaluation Metric**
- F1-Score (chosen due to class imbalance)

---

## Project Structure

```
Sentiment_Analysis_Project/
│
├── data/
│   └── data.csv
│
├── artifacts/
│   ├── vectorizer.pkl
│   ├── sentiment_model.pkl
│   └── model_metadata.json
│
├── src/
│   ├── config.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── train.py
│   ├── evaluate.py
│   ├── model_registry.py
│   └── inference.py
│
├── app.py
├── requirements.txt
├── README.md
└── run_training.py
```

---


---

## Streamlit Web Application

The deployed web app allows users to:
- Enter a custom product review
- Get **real-time sentiment prediction**
- View model information and performance (F1-score)

---

## How to Run Locally

### 1. Clone the Repository

```
git clone https://github.com/Avik-Das-567/Sentiment-Analysis-Flipkart-Product-Reviews.git
cd Sentiment-Analysis-Flipkart-Product-Reviews
```

### 2. Create Virtual Environment & Install Dependencies

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Train the Model

```
python run_training.py
```

### 4. Run Streamlit App

```
streamlit run app.py
```

---

## Deployment

- Platform: **Streamlit Community Cloud**

- Deployment via GitHub repository

- Artifacts committed for fast startup and inference-only runtime

---

## Key Highlights

- End-to-end MLOps workflow

- Clean modular code structure

- Real-world dataset

- Production-style deployment

- Easily extensible to advanced NLP models (BERT, Transformers)
