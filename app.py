import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Initialize OpenAI client
API_KEY = os.getenv('API_KEY')
client = OpenAI(api_key=API_KEY)

# Define the ask function to interact with OpenAI API


def ask(question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

# Route to render the HTML template


@app.route("/")
def index():
    return render_template("index.html")

# Route to handle user's chat message and return bot's response


@app.route("/chat", methods=["POST"])
def chat():
    msg = request.form["msg"]
    answer = ask(msg)
    return jsonify({"content": answer})


if __name__ == "__main__":
    app.run(debug=True)
