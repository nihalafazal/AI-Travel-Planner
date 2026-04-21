# AI Travel Idea Generator ✈️

A beginner-friendly Flask web application that generates personalized travel ideas, itineraries, packing lists, and image concepts using the Google Gemini API.

## Features
- Choose your budget, travel days, and destination type (Beach, City, Mountains).
- AI-generated trip suggestions tailored to your preferences.
- Structured itineraries based on the number of travel days and essential packing checklists.
- Clean and modern HTML/CSS frontend.

## Setup Instructions

1. Clone this repository to your local machine.
2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory (or use the one provided) and add your Google Gemini API Key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```
   *You can get a Gemini API key from [Google AI Studio](https://aistudio.google.com/).*

## Run Instructions (Local)

1. Run the Flask app from your terminal:
   ```bash
   python app.py
   ```
2. Open your web browser and go to `http://127.0.0.1:5000/`.

## Deployment Steps (Vercel & GitHub)

1. **GitHub Upload**:
   - Create a new repository on GitHub.
   - Push all the code including `app.py`, `vercel.json`, `requirements.txt`, etc., to this repository. Do NOT upload the `.env` file with your real API key.
2. **Deploy via Vercel**:
   - Go to [Vercel](https://vercel.com/) and log in (you can sign in with your GitHub account).
   - Click **Add New Project**.
   - Import the GitHub repository you just created.
   - In the "Configure Project" screen, go down to **Environment Variables**.
   - Add a new variable: 
     - Name: `GEMINI_API_KEY` 
     - Value: your actual Google API key.
   - Click **Deploy**. Vercel will automatically use `vercel.json` and `requirements.txt` to build and launch your Flask backend as a Serverless application!

Enjoy planning your travels!
