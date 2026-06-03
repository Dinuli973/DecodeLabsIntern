print("Rule Based Chatbot")
print("Type 'bye' to exit")

while True:
    user_input = input("Input:").lower()

    #Greetings
    if user_input == "hello" or user_input == "hi":
        print("Hello! How can I help you Today?")
    elif user_input=="Good Morning":
        print("Good Morning")
    elif user_input=="Good Afternoon":
        print("Good Afternoon")


