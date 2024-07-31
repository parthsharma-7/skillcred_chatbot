Gemini-Pro Q&A Chatbot
This project is a Streamlit-based web application that leverages Google's Gemini-Pro AI model to create an interactive Q&A chatbot. Users can ask questions, receive AI-generated responses, and view their chat history.

Features
Interactive Q&A interface powered by Google's Gemini-Pro AI model Real-time streaming of AI responses Chat history sidebar for easy reference to previous interactions Clean and intuitive user interface

Prerequisites
Python 3.7 or higher A Google API key for accessing the Gemini-Pro model

Installation
Install the required dependencies: pip install -r requirements.txt

Create a .env file in the project root and add your Google API key: GOOGLE_API_KEY=your_api_key_here

Usage
Run the Streamlit app: streamlit run app.py

Open your web browser and navigate to the URL provided by Streamlit (usually http://localhost:8501). Enter your question in the input field and click "Ask the question" to receive a response from the AI. View your chat history in the sidebar on the left side of the screen.

Project Structure
app.py: The main Streamlit application file containing the Q&A chatbot logic. requirements.txt: List of Python dependencies required for the project. .env: Contains your Google API key.
