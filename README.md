# AI-First CRM HCP Interaction Logging System


## Project Overview


This project is an AI-powered CRM system for Healthcare Professional (HCP) interaction logging.


The user communicates with an AI assistant instead of manually filling the interaction form. The AI agent extracts information, selects tools, and updates the interaction details automatically.


## Architecture


User
?
AI Chat Assistant
?
LangGraph Agent
?
CRM Tools
?
Interaction Data
?
Form Update


## Technologies Used


- Python
- LangGraph
- LLM
- FastAPI
- React
- Redux
- Database


## LangGraph Tools


### 1. Log Interaction
Creates a new HCP interaction from natural language input.


### 2. Edit Interaction
Updates only selected fields based on user corrections.


### 3. Search HCP
Finds HCP information from records.


### 4. Generate Follow-up
Creates recommended next actions.


### 5. Interaction Analysis
Provides insights from interaction data.


## Key Features


- AI-controlled form filling
- Natural language interaction logging
- Sentiment detection
- Follow-up suggestions
- HCP search
- Interaction analytics


## Demo Flow


1. User enters interaction details through AI chat.
2. LangGraph agent selects the required tool.
3. Tool updates the interaction data.
4. Form displays the updated information.


## Conclusion


This project demonstrates how AI agents can automate CRM workflows and reduce manual data entry.

