from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set API key and base URL for DeepSeek
openai.api_key = os.getenv("DEEPSEEK_API_KEY")
openai.api_base = "https://api.deepseek.com/v1"  # Adjust the base URL if required by DeepSeek

if not openai.api_key:
    raise ValueError("API key not found. Please set the DEEPSEEK_API_KEY environment variable in your .env file.")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json.get('message')
    if user_message:
        try:
            # Call the DeepSeek (OpenAI) API for chatbot response
            response = openai.ChatCompletion.create(
                model="deepseek-chat",  # Use the model name specific to DeepSeek
                messages=[
                    {"role": "system", "content": "You are a helpful assistant"},
                    {"role": "user", "content": user_message},
                ]
            )
            bot_response = response['choices'][0]['message']['content']
        except Exception as e:
            bot_response = "Sorry, I encountered an error: " + str(e)
        return jsonify({"response": bot_response})
    return jsonify({"response": "I didn't understand that. Can you try again?"})

if __name__ == '__main__':
    app.run(debug=True)
