# 🔁 Duplicate Question Detector

This is a **Streamlit web app** that intelligently detects whether two user-entered questions are duplicates — useful for Q&A platforms, forums, or customer support systems.

🚀 **Live Demo**:  
[Click here to try it out](https://duplicate-quetion-pair-cvaq4vhgijr32kldstpcu8.streamlit.app/)

---

## 📌 Overview

This app uses a **trained machine learning model** (Random Forest) to detect semantic similarity between questions. It extracts handcrafted and vector-based features to compare them intelligently.

---

## 🧠 Features

✅ Clean, decontract, and lemmatize text  
✅ Token-based and length-based features  
✅ Fuzzy matching with FuzzyWuzzy  
✅ Sentence vectorization using **Word2Vec**  
✅ Trained RandomForest model (compressed using `joblib`)  
✅ Deployed on **Streamlit Cloud**

---

## 🛠 Technologies Used

| Category         | Libraries / Tools                  |
|------------------|------------------------------------|
| Web UI           | Streamlit                          |
| NLP              | NLTK, BeautifulSoup, FuzzyWuzzy    |
| Vectorization    | Gensim (Word2Vec)                  |
| ML Model         | Scikit-learn (Random Forest)       |
| Model Saving     | Joblib, Pickle                     |
| Deployment       | Streamlit Cloud                    |

---

## 🖼️ Demo Screenshots

### 🔹 App Home Page and result

![Home](git_read_me.png)


## 📦 Installation (Local)

```bash
git clone https://github.com/Pdevshali/Duplicate-Quetion-Pair.git
cd Duplicate-Quetion-Pair
pip install -r requirements.txt
streamlit run app.py
