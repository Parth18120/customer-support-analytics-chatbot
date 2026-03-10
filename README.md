Customer Support Analytics Chatbot
Overview

This project is a simple NLP chatbot built using Python and Flask. The main goal was to experiment with natural language processing and see how a chatbot can help answer common customer questions automatically.

The chatbot uses a machine learning model to classify user questions into different intents and respond with the appropriate answer. I also added logging and analytics so interactions can be analyzed later to understand common questions and improve responses.

This project helped me practice working with text data, machine learning models, and building a small web application.

Features

NLP based intent classification

Confidence scoring for predictions

Fallback response when confidence is low

Simple web interface using Flask

Logging of user interactions

Basic analytics on chatbot conversations

Technologies Used

Python

Flask

Scikit-learn

NLTK

HTML / CSS

JSON for training data

How It Works

User enters a question in the chatbot interface.

The text is cleaned and converted into features using CountVectorizer.

A Multinomial Naive Bayes model predicts the intent of the question.

If the confidence is high enough, the chatbot returns a response.

If confidence is low, a fallback message is shown.

The interaction is logged so it can be analyzed later.

Project Structure
chatbot_project/
│
├── app.py
├── model.py
├── intents.json
├── analytics.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── tests/
    └── test_model.py
Example Use Case

This chatbot could be used for:

answering common FAQ questions

customer support automation

internal helpdesk assistants

It can also be extended with more training data or connected to external APIs.

Installation

Clone the repository

git clone https://github.com/yourusername/customer-support-analytics-chatbot.git
cd customer-support-analytics-chatbot

Install dependencies

pip install -r requirements.txt

Run the application

python app.py

Open in browser

http://localhost:5000
