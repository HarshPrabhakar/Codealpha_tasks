import random
import spacy
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Load spaCy's English language model
nlp = spacy.load('en_core_web_sm')



# Sample conversation data
corpus = [
    "Hello, how can I help you?",
    "Hi there!",
    "What is your name?",
    "I am a chatbot created to assist you.",
    "What do you do?",
    "I provide information and chat with you.",
    "Tell me a joke.",
    "Why don't scientists trust atoms? Because they make up everything!",
    "Goodbye",
    "See you later!"
]

# Tokenization (split text into words)
def tokenize(text):
    return nltk.word_tokenize(text.lower())

# Lemmatization (reduce words to their base form)
lemmatizer = nltk.WordNetLemmatizer()
def lemmatize(tokens):
    return [lemmatizer.lemmatize(token) for token in tokens]

# Greeting function
def greet(user_input):
    greetings = ["hi", "hello", "hey", "howdy"]
    responses = ["Hello!", "Hi there!", "Hey!", "Hi! How can I assist you?"]
    for word in user_input.split():
        if word.lower() in greetings:
            return random.choice(responses)
    return None

# Function to find the best match from the corpus
def generate_response(user_input):
    # Combine user input with the corpus
    corpus_with_input = corpus + [user_input]
    
    # Vectorize the corpus using TF-IDF
    vectorizer = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(corpus_with_input)
    
    # Calculate cosine similarity between user input and the corpus
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    # Find the index of the most similar response
    response_index = np.argmax(similarity_scores)
    
    # Return the most similar response from the corpus
    return corpus[response_index]

# Chatbot response function
def chatbot_response(user_input):
    # Check for greeting
    greeting = greet(user_input)
    if greeting:
        return greeting
    
    # Generate response
    response = generate_response(user_input)
    return response

def chat():
    print("Chatbot: Hi, I'm your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            response = chatbot_response(user_input)
            print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    chat()
