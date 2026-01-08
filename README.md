# AutoJudge: Automated Difficulty Prediction for Programming Problems

## 📌 Overview
AutoJudge is a machine learning–based system that automatically predicts the difficulty of programming problems using their textual descriptions. Difficulty labeling on coding platforms is often subjective and inconsistent. This project addresses that challenge by providing an automated, scalable, and interpretable solution that predicts both a categorical difficulty level (Easy / Medium / Hard) and a continuous numerical difficulty score.

The system combines Natural Language Processing (NLP) techniques with supervised machine learning models and is accompanied by an interactive web interface built using Streamlit.

---

## 📂 Dataset
The dataset consists of programming problems stored in **JSONL (JSON Lines) format**, where each record represents a single problem.

### Dataset Attributes
- Title  
- Problem Description  
- Input Description  
- Output Description  
- Difficulty Class (`problem_class`: Easy / Medium / Hard)  
- Difficulty Score (`problem_score`: numerical value)

The dataset includes problems of varying complexity and exhibits class imbalance, with a higher proportion of Hard problems.

---

## ⚙️ Methodology

### 🔹 Data Preprocessing
- Missing textual values replaced with empty strings
- All text fields combined into a single `combined_text` representation
- Text normalized through lowercasing and whitespace cleaning

### 🔹 Feature Engineering
- **TF-IDF Vectorization** (unigrams and bigrams) for semantic representation
- Handcrafted linguistic features:
  - Text length
  - Mathematical symbol count
  - Algorithm keyword frequencies (e.g., graph, recursion, dynamic programming)

All features are combined into a sparse feature matrix for model training.

---

## 🤖 Models Used

### Classification Models (Difficulty Class)
- Logistic Regression  
- Balanced Logistic Regression  
- **Linear Support Vector Machine (Final Model)**  

### Regression Model (Difficulty Score)
- **Ridge Regression**

Linear SVM was selected as the final classifier due to its superior balanced performance across classes, while Ridge Regression was chosen for its robustness on high-dimensional sparse data.

---

## 📊 Evaluation Metrics

### Classification
- Accuracy  
- Confusion Matrix  
- Precision, Recall, F1-score  
- Macro F1-score  

**Final Classification Accuracy:** ~0.56  
**Macro F1-score:** ~0.50  

### Regression
- Mean Absolute Error (MAE): ~1.65  
- Root Mean Squared Error (RMSE): ~1.98  

These results demonstrate meaningful performance given the subjective nature of difficulty estimation.

---

## 🌐 Web Interface
A web-based interface is implemented using **Streamlit** to demonstrate real-time predictions.

### Features
- Input problem description, input format, and output format
- Predicts:
  - Difficulty Class (Easy / Medium / Hard)
  - Numerical Difficulty Score
- Runs locally without deployment or hosting

---

## 🎥 Demo Video

A 2–3 minute demonstration video showcasing the project overview, model approach, and the working web interface is available at the link below:

🔗 **Demo Video:** https://your-video-link-here

---

## 👤 Author Details

Name: Jampa Sri Pramodhitha

Enrollment Number: 23113075

Program: B.Tech (3rd Year)

Department: Civil Engineering

---
