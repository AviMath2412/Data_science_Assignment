# Week 8 — Rule-Based Agentic AI System

A lightweight, rule-based **Agentic AI System** built from scratch in Python. The system demonstrates the core concepts of agentic architecture: input routing, validation, verification, step-by-step logging, and tool calling.

---

## 🏛️ System Architecture

The project is structured into two main components: the **Agent Core** (handling orchestration, routing, and verification) and the **Tool Suite** (specialized modules for task execution).

```
week8_Avi_Mathur/
├── agent/                  # Agent Core Orchestration
│   ├── __init__.py
│   ├── router.py           # Routes queries to appropriate tools
│   ├── validator.py        # Validates user inputs and schema constraints
│   ├── verifier.py         # Verifies final output correctness
│   ├── logger.py           # Logs agent reasoning and tool executions
│   └── memory.py           # Short-term memory for agent conversations
├── tools/                  # Extensible Tool Suite
│   ├── __init__.py
│   ├── calculator.py       # Safe mathematical expression evaluator
│   ├── keyword_extractor.py# NLTK-based text keyword extractor
│   └── text_statistics.py  # Text metrics calculator (word/char count, readability)
├── tests/                  # Test suite
│   └── test_agent.py       # Runs verification and tests
├── docs/
│   └── quiz_answers.md     # Agentic AI conceptual quiz answers
├── requirements.txt        # Python dependencies
└── main.py                 # Main application entry point
```

---

## ⚙️ Components Description

### 🧠 Agent Core
*   **`router.py`**: Analyzes user input using rule-based/regex pattern matching or keyword association to determine the correct tool to invoke.
*   **`validator.py`**: Ensures the input received is formatted correctly and safe to process before invoking any tool.
*   **`verifier.py`**: Performs post-execution checks on tool outputs to ensure they are logically sound and directly answer the user's prompt.
*   **`logger.py`**: Formats and logs agent executions, showing the "Thought -> Action -> Observation -> Final Answer" loop.
*   **`memory.py`**: Provides session-based memory using a deque to track the agent's query and response history.

### 🛠️ Tool Suite
*   **Calculator (`calculator.py`)**: Parses and evaluates mathematical expressions safely using Python's Abstract Syntax Trees (`ast`), preventing remote code execution vulnerabilities from generic `eval()`.
*   **Keyword Extractor (`keyword_extractor.py`)**: Uses `nltk` to tokenize text, remove stopwords/punctuation, and extract top frequency-based keywords.
*   **Text Statistics (`text_statistics.py`)**: Analyzes textual inputs to generate stats like total word count, character count, and average word length.

---

## 🚀 Setup & Installation

### 1. Set Up Virtual Environment
Create and activate a local virtual environment in the `week8_Avi_Mathur` directory:
```bash
# Navigate to directory
cd week8_Avi_Mathur

# Create virtual environment
python -m venv .venv

# Activate virtual environment (macOS/Linux)
source .venv/bin/activate
```

### 2. Install Dependencies
Install all required packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 3. Run Tests
Execute the agent tests using the virtual environment's python interpreter:
```bash
python tests/test_agent.py
```

### 4. Run the Interactive CLI Agent
Run the main agent application to start the interactive prompt loop:
```bash
python main.py
```
*   Type your queries (e.g., `Calculate (100 + 50) / 3`, `Analyze this simple text`, `Extract keywords from this description`).
*   Type `history` to print out the list of previous queries and responses stored in memory.
*   Type `exit` to close the agent.
