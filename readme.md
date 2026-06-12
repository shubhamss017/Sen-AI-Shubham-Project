# Sen-AI-Shubham-Project

# AI-Powered CRM Agent

## Overview

This project is an AI-powered CRM Agent designed to help customer support teams process and manage customer emails efficiently.

The system automatically analyzes incoming emails, understands customer intent, retrieves relevant company policies using Retrieval-Augmented Generation (RAG), generates suggested responses, determines whether human intervention is required, and maintains a complete reasoning trace for transparency.

The goal of this project is to demonstrate how Large Language Models (LLMs), vector databases, and traditional backend systems can be combined to automate customer support workflows.


## Features

### Email Ingestion

* Loads customer emails from the provided dataset
* Stores emails in PostgreSQL
* Preserves thread relationships between conversations

### Contact Management

* Maintains customer profiles
* Stores account-related information
* Links contacts with email conversations

### Thread Management

* Groups emails into conversation threads
* Retrieves complete customer interaction history
* Provides context for AI decision-making

### AI Email Analysis

The system automatically identifies:

* Email Category
* Customer Sentiment
* Priority Level
* Escalation Requirement
* Confidence Score
* Summary of Customer Issue

Example:

```json
{
  "category": "Refund Request",
  "sentiment": "Negative",
  "priority": "High",
  "confidence": 0.91,
  "requires_escalation": true
}
```

### Retrieval-Augmented Generation (RAG)

The CRM agent uses ChromaDB and Sentence Transformers to retrieve relevant information from:

* Refund Policies
* SLA Documents
* Escalation Rules
* Internal Knowledge Base

This allows the AI to generate responses based on company policies rather than relying solely on the LLM.

### Suggested Response Generation

The AI generates professional customer support replies based on:

* Customer email content
* Previous conversation history
* Retrieved knowledge base documents

Example:

```text
Dear Customer,

Thank you for contacting us.

We understand your concern regarding the service interruption.
According to our refund policy, refund requests submitted within 14 days are eligible for review.

Our support team will investigate the issue and provide an update shortly.

Regards,
Customer Support Team
```

### Human Review Detection

The system automatically flags emails for human review when:

* Confidence score is below 0.70
* Critical issues are detected
* Escalation is recommended by the AI

This ensures that sensitive cases are reviewed by support agents before action is taken.

### Agent Reasoning Trace

Every AI decision is accompanied by a reasoning log.

Example:

```json
[
  {
    "step": 1,
    "thought": "Analyze customer email",
    "observation": "Negative sentiment detected"
  },
  {
    "step": 2,
    "thought": "Search knowledge base",
    "observation": "Refund policy retrieved"
  },
  {
    "step": 3,
    "thought": "Determine action",
    "observation": "Escalation recommended"
  }
]
```

This improves transparency and auditability.

### Action Management

Agent decisions are stored in the database including:

* Recommended Action
* Suggested Response
* Confidence Score
* Escalation Reason
* Reasoning Log

## Technology Stack

### Backend

* FastAPI
* Python

### Database

* PostgreSQL

### Vector Database

* ChromaDB

### Embedding Model

* Sentence Transformers
* all-MiniLM-L6-v2

### Large Language Model

* Groq API
* Llama 3.3 70B Versatile

### Frontend

* Streamlit

## System Architecture

```text
Customer Email
       │
       ▼
Email Ingestion
       │
       ▼
PostgreSQL Database
       │
       ▼
Email Analysis (LLM)
       │
       ├─────────────► Category
       ├─────────────► Sentiment
       ├─────────────► Priority
       └─────────────► Confidence
       │
       ▼
RAG Retrieval
(ChromaDB)
       │
       ▼
Reasoning Engine
       │
       ▼
Agent Decision
       │
       ├─────────────► Suggested Reply
       ├─────────────► Escalation
       └─────────────► Human Review Check
       │
       ▼
Actions Table
```

## Database Schema

### Emails

| Column     | Description         |
| ---------- | ------------------- |
| id         | Email ID            |
| message_id | Unique Message ID   |
| thread_id  | Conversation Thread |
| sender     | Customer Email      |
| subject    | Email Subject       |
| body       | Email Content       |
| category   | AI Category         |
| sentiment  | AI Sentiment        |
| priority   | AI Priority         |
| summary    | Email Summary       |


### Contacts

| Column       | Description    |
| ------------ | -------------- |
| id           | Contact ID     |
| email        | Customer Email |
| name         | Customer Name  |
| account_type | Account Type   |


### Actions

| Column            | Description            |
| ----------------- | ---------------------- |
| id                | Action ID              |
| email_id          | Related Email          |
| action_type       | Agent Decision         |
| confidence        | AI Confidence          |
| escalation_reason | Escalation Explanation |
| proposed_content  | Suggested Reply        |
| reasoning_log     | Agent Reasoning        |


## API Endpoints

### Analyze Email

```http
POST /api/analyze
```

Analyzes customer emails using the LLM.


### Thread Details

```http
GET /api/thread/{thread_id}
```

Returns thread history.


### Contact Profile

```http
GET /api/contact/{contact_id}
```

Returns customer information.


### RAG Search

```http
GET /api/rag/search
```

Searches internal knowledge base.


### Agent Execution

```http
POST /api/agent/execute/{email_id}
```

Runs the complete CRM agent workflow.

Returns:

```json
{
  "category": "Refund Request",
  "sentiment": "Negative",
  "priority": "High",
  "confidence": 0.91,
  "requires_human": true,
  "action_type": "Escalate",
  "summary": "...",
  "suggested_reply": "..."
}
```


## Streamlit Dashboard

A Streamlit dashboard is provided to demonstrate the system visually.

Features:

* Email Analysis
* AI Decision Display
* Confidence Visualization
* Suggested Reply Generation
* RAG Search
* Agent Output Monitoring

Run:

```bash
streamlit run app.py
```


## Installation

### Clone Repository

```bash
git clone <repository-url>
cd crm-agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create:

```env
DATABASE_URL=postgresql://username:password@localhost/crm_db
GROQ_API_KEY=your_groq_api_key
```

### Run Backend

```bash
uvicorn app.main:app --reload
```

### Run Streamlit Dashboard

```bash
streamlit run app.py
```


## Future Improvements

* Multi-Agent Workflow
* Real-Time Email Monitoring
* Advanced Entity Extraction
* Analytics Dashboard
* Web Intelligence Integration
* Automated Ticket Creation


## Author

Developed as part of an AI CRM Agent assignment demonstrating the integration of:

* Large Language Models
* Retrieval-Augmented Generation
* PostgreSQL
* FastAPI
* ChromaDB
* Streamlit

for intelligent customer support automation.
