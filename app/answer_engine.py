def generate_answer(question: str):
    # For now, return dummy content
    if "gpt-4o" in question.lower():
        answer = "Use `gpt-3.5-turbo-0125`, as mentioned in the course instructions."
        links = [
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
                "text": "Use the model that’s mentioned in the question."
            },
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
                "text": "You just need to use a tokenizer to get token count and calculate cost."
            }
        ]
    else:
        answer = "Thank you for your question! Please refer to the official discourse threads."
        links = []

    return answer, links
