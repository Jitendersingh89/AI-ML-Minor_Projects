
# AI Text Summarizer using T5 Transformer 🚀

An end-to-end AI-powered text summarization web application built using **Hugging Face Transformers**, **PyTorch**, and **FastAPI**. The application generates concise summaries from long-form text through a clean web interface.

---

## 📌 Features

- Fine-tuned T5 Transformer for abstractive text summarization
- FastAPI backend for model inference
- Interactive HTML frontend
- Text preprocessing and cleaning
- GPU (CUDA/MPS) and CPU support
- Hugging Face model hosting
- REST API endpoint for summarization

---

## 🛠️ Tech Stack

- Python
- PyTorch
- Hugging Face Transformers
- FastAPI
- Jinja2
- HTML
- Uvicorn

---

## 📂 Project Structure

```
Text-Summarizer-Using-T5-FastAPI/
│
├── app.py
├── requirements.txt
├── README.md
│── index.html
```

---

## 🤖 Model

The fine-tuned T5 model is hosted on Hugging Face.

**Model Repository**

https://huggingface.co/Jitender89/t5-text-summarizer-samsum

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Jitendersingh89/Text-Summarizer-Using-T5-FastAPI.git
```

Move into the project directory

```bash
cd Text-Summarizer-Using-T5-FastAPI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python -m uvicorn app:app --reload
```

Open your browser

```
http://127.0.0.1:8000
```

---

## 🧠 Model Training

The model was fine-tuned using the **SAMSum Dialogue Summarization Dataset**.

Training pipeline includes:

- Data preprocessing
- Text cleaning
- Tokenization using T5Tokenizer
- Fine-tuning T5
- Model evaluation
- Saving the trained model

The complete training workflow is available in: text_summarizer.ipynb

## 👨‍💻 Author

**Jitender Singh**

GitHub:
https://github.com/Jitendersingh89

Hugging Face:
https://huggingface.co/Jitender89

---

## ⭐ If you found this project useful, consider giving it a star!
