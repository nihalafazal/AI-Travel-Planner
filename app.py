import os
import csv
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize Groq client. Check both environment variable names just in case!
api_key = os.getenv("GROQ_API_KEY") or os.getenv("GEMINI_API_KEY")

try:
    client = Groq(api_key=api_key)
except Exception as e:
    client = None
    print(f"Warning: Groq Client not initialized: {e}")

def load_prompt_template():
    try:
        with open('prompts/travel_prompt.txt', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "You are an expert AI Travel Planner. Suggest a destination for a {budget} budget {type} trip for {days} days. Provide a suggestion, a 3-day itinerary, a packing checklist, and an image idea description."

def read_destinations():
    destinations = []
    try:
        with open('dataset/destinations.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                destinations.append(row)
    except FileNotFoundError:
        pass
    return destinations

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        budget = data.get('budget', 'Medium')
        days = data.get('days', 3)
        dest_type = data.get('type', 'city')
        
        prompt_template = load_prompt_template()
        prompt = prompt_template.format(type=dest_type, budget=budget, days=days)
        
        if not client:
            raise Exception("Groq client is not initialized. Please check your API key in .env")
            
        # Call Groq API
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.1-8b-instant",
        )
        
        response_text = chat_completion.choices[0].message.content
        
        return jsonify({
            'success': True,
            'result': response_text
        })
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
