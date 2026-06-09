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

    #Questions
    elif user_input=="How are you":
        print("I am Fine. Thank you for asking")
    elif user_input=="what's your name":
        print("My name is ChatBot")
    elif user_input=="What's your favorite color":
        print("My favorite color is blue")

    #exit
    elif user_input=="bye":
        print("Goodbye! Have a nice day.")
        break

    else:
        print("Invalid Input.I don't understand that.")
