# Customer Support Analytics Chatbot

A portfolio-ready Flask application that combines **FAQ automation** with **conversation analytics**. It classifies user intent, responds with high-confidence answers, logs every interaction, and generates simple analytics on conversation quality.

## Why this project matters

This project is designed to show business value, not just code:

- **Automates customer support FAQs** to reduce repetitive manual work.
- **Tracks chatbot usage and fallback rate** so teams can improve content quality.
- **Uses confidence scoring** to avoid incorrect answers and escalate unclear queries.
- **Creates analytics-ready logs** that can be used for reporting and service improvement.

## Business use case

A support team receives repetitive questions about orders, refunds, hours, shipping, and account help. This chatbot answers common questions instantly and logs each interaction. The logs can be analyzed to identify:

- top customer intents
- unresolved questions
- fallback rate
- response confidence trends
- content gaps for FAQ updates

## Features

- Flask web app with a clean chat UI
- Intent classification using `CountVectorizer + MultinomialNB`
- Confidence threshold with fallback handling
- CSV-based interaction logging
- Analytics summary script for conversation quality monitoring
- Unit tests for core prediction behavior
- Modular project structure

## Project structure

```text
customer-support-analytics-chatbot/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── data/
│   ├── intents.json
│   └── chat_logs.csv
├── chatbot/
│   ├── __init__.py
│   ├── model.py
│   ├── preprocessing.py
│   ├── logging_utils.py
│   └── analytics.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── tests/
    └── test_model.py
```

## Skills demonstrated

- Python
- Flask
- NLP preprocessing
- Scikit-learn classification
- Data logging and monitoring
- Basic product analytics
- Error handling and modular design
- README / documentation quality

## Setup

```bash
git clone <your-repo-url>
cd customer-support-analytics-chatbot
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Run analytics summary

```bash
python -m chatbot.analytics
```

This generates:
- total conversations
- top intents
- fallback rate
- average confidence

## Run tests

```bash
pytest -q
```

## Example resume bullets

- Built a Flask-based customer support chatbot using Python and scikit-learn to automate FAQ handling and improve response consistency.
- Added confidence scoring, fallback handling, and interaction logging to improve answer quality and enable chatbot performance analysis.
- Designed an analytics workflow to monitor top intents, fallback rate, and response confidence, turning chatbot logs into actionable service insights.

## Suggested next upgrades

- Add a Power BI dashboard connected to the chatbot log file
- Add sentiment detection for user feedback
- Replace bag-of-words model with sentence embeddings
- Deploy on Render or Azure App Service
- Add admin page for unanswered questions
