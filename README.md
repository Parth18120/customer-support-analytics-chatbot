# Customer Support Analytics Chatbot
## Business Problem

Customer support teams receive many repetitive questions from users.
This project demonstrates how a machine learning based chatbot can help automate responses to common questions and reduce manual support workload.

## Overview
This project is a simple NLP chatbot built using **Python** and **Flask**.  
The goal was to experiment with natural language processing and build a small application that can answer common customer questions automatically.

The chatbot classifies user questions into different **intents** and returns the appropriate response.  
User interactions are logged so they can be analyzed later to understand common questions and improve responses.

This project helped me practice working with **text data, machine learning models, and building a small web application**.

## Features
- NLP-based intent classification
- Confidence scoring for predictions
- Fallback response when confidence is low
- Simple web interface using Flask
- Logging of user interactions
- Basic analytics on chatbot conversations

## Technologies Used
- Python
- Flask
- Scikit-learn
- NLTK
- HTML / CSS
- JSON for training data

## How It Works
1. The user enters a question in the chatbot interface.
2. The text is cleaned and converted into features using **CountVectorizer**.
3. A **Multinomial Naive Bayes** model predicts the intent of the question.
4. If the prediction confidence is high enough, the chatbot returns the appropriate response.
5. If confidence is low, a fallback message is shown.
6. The interaction is logged so it can be analyzed later.

## Project Structure

```
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
```

## Example Use Case
This chatbot could be used for:

- Answering common FAQ questions  
- Customer support automation  
- Internal helpdesk assistants  

It can also be extended with more training data or connected to external APIs.

## Installation

Clone the repository

```bash
git clone https://github.com/Parth18120/customer-support-analytics-chatbot.git
cd customer-support-analytics-chatbot
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open in browser

```
http://localhost:5000
```

## Future Improvements
Some things I would like to improve in the future:

- Deploy the chatbot online
- Improve intent classification using more advanced NLP models
- Store conversations in a database
- Build a dashboard to visualize chatbot analytics

## What I Learned
Working on this project helped me understand:

- How NLP models classify text
- How to build a small ML application
- How to integrate a model into a web interface
- How to log and analyze user interactions
