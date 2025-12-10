# 🚀 Customer Support Chatbot (NLP + ML)  
### A Machine Learning Project by *Vidit Kumar*  
### Repository: *FUTURE_ML_03*

<p align="center">
  <img src="Chatbot_Homepage.png" alt="Chatbot Homepage" width="650"/>
</p>

---

## 📖 Project Overview

The *Customer Support Chatbot* is an NLP-powered system designed to automatically respond to customer queries using historical customer–agent conversations from Twitter.  

It uses:

- *TF-IDF Vectorization*  
- *Cosine Similarity Matching*  
- *Custom text preprocessing pipeline*  
- *Streamlit Interface*

This chatbot can answer common customer support questions instantly and can be extended to any domain with FAQ-style data.

---

## 🎯 Project Objectives

- Build an end-to-end NLP pipeline  
- Clean and preprocess real-world noisy text data  
- Train a vector-based retrieval model  
- Develop a modular chatbot engine  
- Deploy as a fully interactive web app using *Streamlit*

---

## 🧠 Key Features

### ✅ Smart Text Preprocessing  
Removes URLs, usernames, special characters, and normalizes text for uniform processing.

### ✅ TF-IDF + Cosine Similarity Engine  
Finds the closest answer from 1.2M+ cleaned Q&A pairs.

### ✅ Fallback Response  
When similarity is too low, the chatbot returns a polite fallback message instead of giving incorrect answers.

### ✅ Streamlit UI  
A clean, modern interface where users can ask any customer support–related question.

---

## 🛠 Tech Stack

| Component | Technology |
|----------|------------|
| Programming | Python |
| NLP | Scikit-learn (TF-IDF, Cosine Similarity) |
| Data Cleaning | Regex, Pandas |
| Deployment | Streamlit |
| Model Storage | Pickle |

---

## 📂 Project Structure


FUTURE_ML_03/
│
├── app/
│   └── app.py                 # Streamlit UI
│
├── data/
│   ├── raw/                   # Original dataset (twcs.csv)
│   └── processed/             # Cleaned FAQ dataset
│
├── models/
│   ├── vectorizer.pkl         # TF-IDF Vectorizer
│   └── faq_data.pkl           # Cleaned and processed dataframe
│
├── notebooks/
│   ├── 01_eda.ipynb           # Data exploration + cleaning
│   └── 02_model.ipynb         # Model building + save artifacts
│
├── utils/
│   ├── chatbot_engine.py      # Main ML logic
│   └── text_cleaning.py       # Cleaning functions
│
├── README.md                  # Project documentation
└── requirements.txt           # Dependencies


---

## 🏗 System Architecture


          ┌────────────────────┐
          │   User Query       │
          └─────────┬──────────┘
                    │
                    ▼
        ┌────────────────────────┐
        │ Text Cleaning Pipeline │
        └─────────┬──────────────┘
                  │
                  ▼
      ┌──────────────────────┐
      │   TF-IDF Vectorizer  │
      └──────────┬───────────┘
                 │
                 ▼
     ┌────────────────────────┐
     │ Cosine Similarity Match│
     └──────────┬─────────────┘
                │ Best Match
                ▼
      ┌────────────────────────┐
      │  Retrieve Agent Reply  │
      └────────────────────────┘

     (If similarity < threshold → fallback message)


---

## 🎬 Project Demo (GIF)

👉 *Add your Demo GIF here once recorded*


![Demo GIF](demo.gif)


---

## 📸 Screenshots

### 🏠 Chatbot Homepage  
<p align="center">
  <img src="Chatbot_Homepage.png" width="700"/>
</p>

### 💬 Question + Answer Example  
<p align="center">
  <img src="Question+Answer.png" width="700"/>
</p>

### 🔄 Fallback Response Example  
<p align="center">
  <img src="Fallback_Example.png" width="700"/>
</p>

---

## ⚙ Installation & Setup

### 1️⃣ Clone the Repo
bash
git clone https://github.com/Vidit3859/FUTURE_ML_03
cd FUTURE_ML_03


### 2️⃣ Create a virtual environment
bash
python -m venv venv

Activate it:

*Windows*
bash
venv\Scripts\activate


### 3️⃣ Install dependencies
bash
pip install -r requirements.txt


### 4️⃣ Run the app
bash
streamlit run app/app.py


Your chatbot will open at:

👉 http://localhost:8501

---

## 📊 Model Details

### 🔹 TF-IDF Vectorizer  
Transforms text into numerical weights.

### 🔹 Cosine Similarity  
Computes how similar the user query is to all historical questions.

### 🔹 Fallback Handling  
If similarity < *0.2*, the model responds:  
> “I'm not sure about that. Could you rephrase?”

---

## 🚀 Future Improvements

- Integrate deep learning model (Sentence Transformers / BERT)
- Add multi-turn conversation memory  
- Deploy on cloud (Render / HuggingFace / Streamlit Cloud)  
- Add voice-based input  

---

## 👨‍💻 Author

*Vidit Kumar*

- 🔗 LinkedIn: https://linkedin.com/in/viditkumar-in  
- 🐙 GitHub: https://github.com/Vidit3859  

---

## ⭐ Support

If you like this project, please ⭐ the repository!  
Your support motivates further development ❤

---
