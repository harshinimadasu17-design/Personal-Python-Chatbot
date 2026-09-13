# Personal Python Question-Answering Chatbot

A simple **Python Question-Answering Chatbot** that answers Python programming questions using a predefined knowledge base. The chatbot accepts questions in natural language, identifies relevant Python topics using keyword matching, and displays appropriate answers through an interactive Streamlit interface.

## Problem Statement

Develop a simple personal chatbot that can answer questions related to Python programming.

The chatbot allows users to enter Python-related questions in natural language and provides appropriate answers based on a predefined Python knowledge base.

## Objectives

* Develop a simple Python-based chatbot.
* Create a predefined knowledge base containing common Python concepts.
* Accept Python questions in natural language.
* Match user questions with relevant topics.
* Provide appropriate predefined answers.
* Develop an interactive web interface using Streamlit.

## Features

* Python-focused question answering
* Predefined Python knowledge base
* Natural-language keyword matching
* Text preprocessing
* Interactive chat interface
* Chat history
* Example questions
* Clear Chat option
* Handles questions outside the knowledge base

## Technologies Used

* **Python**
* **Streamlit**
* **Regular Expressions (re)**
* **VS Code**
* **Git & GitHub**

## Project Structure

Personal_Python_Chatbot/
│
├── app.py
├── chatbot.py
├── knowledge_base.py
├── requirements.txt
└── README.md

### File Description

| File              | Description                                               |
| ----------------- | --------------------------------------------------------- |
| app.py            | Creates the Streamlit chatbot interface                   |
| chatbot.py        | Contains question processing and matching logic           |
| knowledge_base.py | Stores predefined Python questions, keywords, and answers |
| requirements.txt  | Contains required Python packages                         |
| README.md         | Project documentation                                     |

## How It Works


User enters a question
        ↓
Text preprocessing
        ↓
Keyword matching
        ↓
Search predefined knowledge base
        ↓
Find best matching topic
        ↓
Return appropriate answer
        ↓
Display answer in Streamlit


## Example

**User:**


What is a list in Python?


**Chatbot:**


A list is an ordered and mutable collection in Python.
It can store multiple values and allows duplicate elements.


Another example:

**User:**


What is a function?


**Chatbot:**


A function is a reusable block of code designed to perform
a specific task. Functions are defined using the def keyword.


## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project

```bash
cd Personal_Python_Chatbot
```

### 3. Install the required package

```bash
pip install -r requirements.txt
```

## Run the Application

Run the following command in the terminal:

```bash
streamlit run app.py
```

The Streamlit application will open in your web browser.

## Supported Topics

The chatbot currently contains information about topics such as:

* Python
* Variables
* Lists
* Tuples
* Dictionaries
* Sets
* Functions
* Loops
* For loops
* While loops
* If statements
* Classes
* Objects
* Exception handling
* Modules
* PIP

## Limitations

* The chatbot answers only questions available in its predefined knowledge base.
* It does not generate new answers using a large language model.
* Questions outside the knowledge base may not receive a relevant answer.

## Future Scope

* Expand the Python knowledge base.
* Improve natural-language question matching.
* Add more Python programming examples.
* Add additional programming topics.
* Integrate advanced NLP techniques if required.

## Conclusion

The **Personal Python Question-Answering Chatbot** provides a simple and interactive way for users to ask Python-related questions and receive answers from a predefined knowledge base. The Streamlit interface makes the application easy to use and demonstrates the practical use of Python, text processing, and basic chatbot development.
