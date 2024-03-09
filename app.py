import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

client = OpenAI(
    api_key=API_KEY
)

history = []
system_msg = {
    "role": "system",
    "content": """
You are developing a chatbot to assist users in determining which law applies to their specific condition or situation in India. Your chatbot should be able to provide relevant information about Indian laws based on the user's input.

Here's how your chatbot should function:
1. When a user presents a scenario or condition, the chatbot should analyze the provided information to identify key elements that could determine applicable laws.
2. The chatbot should then search through a database or knowledge base of Indian laws and regulations to find the most relevant law(s) that apply to the given condition.
3. After identifying the relevant law(s), the chatbot should provide a concise explanation or summary of the law(s) and how they relate to the user's condition.
4. If necessary, the chatbot should also offer guidance on further steps or actions that the user may need to take in accordance with the identified law(s).

To achieve this functionality, your chatbot's system role should focus on:
- Understanding natural language input from users, including scenarios, conditions, or questions related to Indian laws.
- Extracting key information and context from user input to facilitate law identification.
- Searching and retrieving relevant information from a database or knowledge base of Indian laws and regulations.
- Formulating clear and informative responses that explain the identified law(s) in a user-friendly manner.
- Providing additional guidance or resources to assist users in understanding and complying with applicable laws.

Use this content prompt to guide the development of your chatbot's system role, ensuring that it effectively addresses the user's needs and provides accurate and helpful information regarding Indian laws.
"""
}


def ask(question):

    question_msg = {
        "role": "user",
        "content": question,
    }
    history.append(question_msg)
    response = client.chat.completions.create(
        messages=history,
        model="gpt-3.5-turbo",
    )
    answer_msg = response.choices[0].message
    history.append(answer_msg)
    return answer_msg.content


while True:
    question = input("You: ")

    if (question == 'quit'):
        break

    answer = ask(question)
    print("\n")
    print(f"Bot: {answer}")
    print("\n")
