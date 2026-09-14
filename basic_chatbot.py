# CodeAlpha Internship
# Task 4: Basic Chatbot
# Domain: Python Programming


def chatbot_response(user_input):
    """
    This function returns a response
    according to the user's input.
    """

    user_input = user_input.lower().strip()

    # Greeting
    if user_input == "hello" or user_input == "hi":
        return "Hi! Nice to meet you."

    # How are you
    elif user_input == "how are you":
        return "I'm fine, thanks!"

    # Name
    elif user_input == "what is your name":
        return "My name is Python Bot."

    # What chatbot can do
    elif user_input == "what can you do":
        return "I can respond to simple predefined messages."

    # Thanks
    elif user_input == "thank you" or user_input == "thanks":
        return "You're welcome!"

    # Help
    elif user_input == "help":
        return "You can say hello, ask how I am, ask my name, or say bye."

    # Goodbye
    elif user_input == "bye":
        return "Goodbye! Have a nice day!"

    # Unknown input
    else:
        return "Sorry, I don't understand that."


# Main program
print("=" * 50)
print("              BASIC PYTHON CHATBOT")
print("=" * 50)

print("Bot: Hello! Welcome to the Basic Chatbot.")
print("Bot: Type 'help' to see what I can do.")
print("Bot: Type 'bye' to exit the chatbot.")

# Chat loop
while True:

    user_input = input("\nYou: ")

    response = chatbot_response(user_input)

    print("Bot:", response)

    # Stop the chatbot when user says bye
    if user_input.lower().strip() == "bye":
        break

print("\nThank you for using the Basic Python Chatbot!")