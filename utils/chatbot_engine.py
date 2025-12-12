import joblib
import pickle
import re
from sklearn.metrics.pairwise import cosine_similarity

class ChatbotEngine:
    def __init__(self, vectorizer_path, faq_data_path):
        # Load vectorizer (prefer joblib, fallback to pickle)
        try:
            self.vectorizer = joblib.load(vectorizer_path)
        except Exception:
            with open(vectorizer_path, "rb") as f:
                self.vectorizer = pickle.load(f)

        # Load FAQ dataframe (prefer joblib, fallback to pickle)
        try:
            self.faq_df = joblib.load(faq_data_path)
        except Exception:
            with open(faq_data_path, "rb") as f:
                self.faq_df = pickle.load(f)

        # Verify required column
        if "clean_question" not in self.faq_df.columns:
            raise KeyError("Expected column 'clean_question' not found in FAQ data")

        # Precompute TF-IDF matrix
        self.tfidf_matrix = self.vectorizer.transform(self.faq_df["clean_question"])

    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r"http\S+", "", text)
        text = re.sub(r"@\w+", "", text)
        text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text

    def get_response(self, user_query):
        clean_query = self.clean_text(user_query)
        user_vec = self.vectorizer.transform([clean_query])

        similarities = cosine_similarity(user_vec, self.tfidf_matrix).flatten()
        best_index = similarities.argmax()
        best_score = float(similarities[best_index])

        if best_score < 0.2:
            return "Sorry, I’m not sure about that. Could you rephrase?"

        return self.faq_df.iloc[best_index]["answer"]