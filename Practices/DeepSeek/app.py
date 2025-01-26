import openai

openai.api_key = "youkey"
openai.api_base = "https://api.deepseek.com"

def chat_with_ai(user_message):
    try:
        response = openai.Completion.create(  # Adjusted method for newer version
            model="deepseek-chat",
            prompt=user_message,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print("AI Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("AI Chatbot: Goodbye!")
            break
        ai_response = chat_with_ai(user_input)
        print(f"AI Chatbot: {ai_response}")
