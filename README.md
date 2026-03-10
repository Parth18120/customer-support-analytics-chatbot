# Customer Support Analytics Chatbot

## Business Problem
Customer support teams receive many repetitive questions from users. This project demonstrates how a machine learning based chatbot can help automate responses to common questions and reduce manual support workload.

## Overview
This project is a simple NLP chatbot built using Python and Flask. The goal was to experiment with natural language processing and build a small application that can answer common customer questions automatically.

The chatbot classifies user questions into different intents and returns the appropriate response. User interactions are logged so they can be analyzed later to understand common questions and improve responses.

This project helped me practice working with text data, machine learning models, and building a small web application.

## Features
* NLP-based intent classification
* Confidence scoring for predictions
* Fallback response when confidence is low
* Simple web interface using Flask
* Logging of user interactions
* Basic analytics on chatbot conversations

## Technologies Used
* Python
* Flask
* Scikit-learn
* NLTK
* HTML / CSS
* JSON for training data

## How It Works
1. The user enters a question in the chatbot interface.
2. The text is cleaned and converted into features using CountVectorizer.
3. A Multinomial Naive Bayes model predicts the intent of the question.
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
├── data/
│   └── sample_chatbot_logs.csv
│
├── templates/
│   └── index.html
│
└── tests/
    └── test_model.py
```

## Dataset Description

This project includes a synthetically generated dataset of **10,000 customer support tickets** (`data/sample_chatbot_logs.csv`) used for analytics, model training experimentation, and dashboard visualisation.

The dataset simulates realistic customer support activity across two years (2023–2024) and covers a wide range of scenarios including billing issues, technical problems, shipping queries, and more.

### Columns

| Column | Description |
|--------|-------------|
| `ticket_id` | Unique ticket identifier (TKT-00001 to TKT-10000) |
| `created_at` | Timestamp when the ticket was created |
| `resolved_at` | Timestamp when the ticket was resolved (blank if unresolved) |
| `category` | Issue category: Billing, Technical, Shipping, Returns, Account, Product, Complaint, General Inquiry |
| `sub_issue` | Specific issue description within the category |
| `product` | Product associated with the ticket (e.g. Laptop Pro, SmartWatch X) |
| `channel` | Support channel used: Email, Chat, Phone, Social Media, App |
| `status` | Current ticket status: Resolved, Pending, Escalated, Closed, In Progress |
| `sentiment` | Customer sentiment detected: Positive, Neutral, Negative |
| `agent_id` | ID of the support agent who handled the ticket (50 unique agents) |
| `resolution_time_mins` | Total time taken to resolve the ticket (in minutes) |
| `first_response_mins` | Time taken for the first agent response (in minutes) |
| `csat_score` | Customer satisfaction score rated 1–5 |
| `priority` | Ticket priority: Low, Medium, High, Critical |
| `resolution_type` | How the ticket was resolved (e.g. Refund Issued, Technical Fix Applied) |
| `escalated` | Whether the ticket was escalated: Yes / No |
| `repeat_contact` | Whether the customer contacted support again: Yes / No |
| `region` | Customer region: North America, Europe, Asia Pacific, Latin America, Middle East |
| `customer_tier` | Customer account tier: Standard, Premium, Enterprise |
| `chatbot_handled` | Whether the chatbot fully handled the ticket without agent intervention: Yes / No |

### Key Statistics
* **10,000 tickets** spanning January 2023 – December 2024
* **8 issue categories** with detailed sub-issues
* **50 support agents** across **5 global regions**
* **8 products** covered
* Realistic CSAT score distribution (skewed positive, as in real support data)
* ~40% of tickets handled by the chatbot, reflecting an automation-first support model
* ~15% escalation rate and ~20% repeat contact rate

### How the Dataset is Used
* **Model training** — the `category` and `sub_issue` fields can be used as intent labels for training or evaluating the NLP classifier
* **Analytics** — `analytics.py` reads this file to generate insights on resolution times, sentiment trends, agent performance, and chatbot effectiveness
* **Testing** — provides a large, consistent dataset for testing edge cases and low-confidence predictions

> **Note:** This dataset is fully synthetic and generated for demonstration purposes. It does not contain any real customer data.

## Example Use Case
This chatbot could be used for:
* Answering common FAQ questions
* Customer support automation
* Internal helpdesk assistants

It can also be extended with more training data or connected to external APIs.

## Installation

**Clone the repository**
```
git clone https://github.com/Parth18120/customer-support-analytics-chatbot.git
cd customer-support-analytics-chatbot
```

**Install dependencies**
```
pip install -r requirements.txt
```

**Run the application**
```
python app.py
```

**Open in browser**
```
http://localhost:5000
```

## Future Improvements
Some things I would like to improve in the future:
* Deploy the chatbot online
* Improve intent classification using more advanced NLP models
* Store conversations in a database
* Build a dashboard to visualize chatbot analytics

## What I Learned
Working on this project helped me understand:
* How NLP models classify text
* How to build a small ML application
* How to integrate a model into a web interface
* How to log and analyze user interactions
