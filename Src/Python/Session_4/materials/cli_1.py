from chatbot import get_responses
def main():
    print("chatbot: hi how can i help u")
    while True:
        user_input = input("user: ").lower()
        response = get_responses(user_input)
        print("chatbot: ", response)

        if user_input == "goodbye":
            break