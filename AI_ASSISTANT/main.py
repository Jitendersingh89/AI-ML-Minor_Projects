from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from groq import Groq

app = Flask(__name__)

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():

    question = request.form.get("question")

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "Act like a helpful personal assistant."
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0.7,
        max_completion_tokens=512,
    )

    answer = response.choices[0].message.content.strip()

    return jsonify({"response": answer}), 200


@app.route("/summarize", methods=["POST"])
def summarize():

    email_text = request.form.get("email")

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """You are an expert email assistant.
Summarize the email in 2-3 concise sentences.
Return only the summary."""
            },
            {
                "role": "user",
                "content": email_text
            }
        ],
        temperature=0.3,
        max_completion_tokens=512,
    )

    summary = response.choices[0].message.content.strip()

    return jsonify({"response": summary}), 200


if __name__ == "__main__":
    app.run(debug=True)
