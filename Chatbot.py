import nltk
import random
import string
import numpy as np

nltk.download('punkt')
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Define some sample responses
responses = {
    "greeting": ["Hello! How can I help you today?", "Hi there! What can I do for you?", "Greetings! How can I assist you?"],
    "help": ["I'm sorry, I don't understand.", "I'm not sure I can help with that.", "Sure, can you provide more information?"],
    "goodbye": ["Goodbye! Have a great day!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "default": ["I'm not sure, But I understand. Can you please rephrase?", "Could you elaborate on that?", "I didn't catch that. Can you repeat?"]
}

# Function to process user input
def preprocess_input(user_input):
    # Lowercase the input and remove punctuation
    user_input = user_input.lower()
    user_input = user_input.translate(str.maketrans('', '', string.punctuation))
    return user_input

# Function to determine the intent
def get_intent(user_input):
    if "hello" in user_input or "hi" in user_input:
        return "greeting"
    elif "help" in user_input:
        return "help"
    elif "bye" in user_input or "goodbye" in user_input:
        return "goodbye"
    elif "thank" in user_input:
        return "thanks"
    else:
        return "default"

# Main chatbot function
def chatbot():
    print("Chatbot: Hello! I am a simple chatbot. [Type 'exit' to end the conversation.]")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        processed_input = preprocess_input(user_input)
        intent = get_intent(processed_input)

        if intent in responses:
            response = random.choice(responses[intent])
        else:
            response = random.choice(responses["default"])

        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
