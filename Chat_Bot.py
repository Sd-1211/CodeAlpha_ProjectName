def chat_bot(user_input):
    user_input=user_input.lower()
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello..How can I help You Today?"
    elif "how are you" in user_input:
        return "Iam fine..thanks!!"
    elif "time" in user_input:
        from datetime import datetime
        return "current time is "+ datetime.now().strftime("%H:%M:%S")
    else:
        return "Iam not sure how to respond to that yet"
print("Chatbot is running! type 'bye' to quit.\n")
while True:
    user=input("You:")
    if "bye" in user.lower():
        print("Chatbot:Goodbye.Have a nice day")
        break
    else:
        print("Chatbot:",chat_bot(user))
