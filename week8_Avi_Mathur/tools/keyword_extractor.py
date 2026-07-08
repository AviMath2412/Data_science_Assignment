import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)
STOP_WORDS = set(stopwords.words("english"))
class KeywordExtractor:
    def extract(self, text: str, top_k: int = 5):
        text = text.lower()
        words = word_tokenize(text)
        keywords = [
            word
            for word in words
            if word not in STOP_WORDS
            and word not in string.punctuation
            and word.isalpha()
        ]
        unique_keywords = []
        for word in keywords:
            if word not in unique_keywords:
                unique_keywords.append(word)
        return unique_keywords[:top_k]