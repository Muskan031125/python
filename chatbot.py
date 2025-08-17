from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        return "That sounds positive! 😄"
    elif polarity < -0.2:
        return "That seems negative... 😟"
    else:
        return "Hmm, that's pretty neutral. 😐"

def chatbot():
    print("Hi! I'm your mood bot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Bot: Goodbye! 😊")
            break
        else:
            response = analyze_sentiment(user_input)
            print("Bot:", response)

chatbot()
