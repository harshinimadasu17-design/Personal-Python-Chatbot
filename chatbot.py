import re
from knowledge_base import knowledge_base 

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text.strip()


def get_answer(question):
    question = preprocess(question)

    best_answer = None
    best_score = 0

    for topic, data in knowledge_base.items():

        score = 0

        for keyword in data["keywords"]:
            keyword = preprocess(keyword)

            if keyword in question:
                score += len(keyword.split())

        if score > best_score:
            best_score = score
            best_answer = data["answer"]

    if best_answer:
        return best_answer

    return (
        "Sorry, I don't have an answer for that question in my Python "
        "knowledge base. Please try asking about Python concepts such as "
        "lists, tuples, dictionaries, functions, loops, classes, or exceptions."
    )