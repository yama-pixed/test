import random


responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you?": ["I'm doing well, thank you!", "I'm great, thanks for asking!"],
    "how are you": ["I'm doing well, thank you!", "I'm great, thanks for asking!"],
    "how are you doing?": ["I'm doing well, thank you!", "I'm great, thanks for asking!"],
    "how are you doing": ["I'm doing well, thank you!", "I'm great, thanks for asking!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "what's your name?": ["I'm a chatbot!", "I don't have a name, I'm just a bot."],
    
}
   

def get_response(message):
    for key in responses:
        if message.lower() in key:
            return random.choice(responses[key])
    return "I'm sorry, I don't understand that question."


print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Chatbot: Goodbye!")
        break
    print("Chatbot:", get_response(user_input))
