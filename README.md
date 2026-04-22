# DataCopilot – AI-Powered Natural Language to SQL Assistant

## 🚀 Overview

DataCopilot is an AI-driven system that converts natural language queries into SQL, executes them on a structured database, and provides human-readable explanations.

Example:

> "Show top 5 customers by revenue in Q3"

✔ Generates SQL
✔ Executes query
✔ Displays results
✔ Explains logic

---

## 🧠 Features

* Natural Language → SQL using LLMs
* Schema-aware query generation
* SQL validation & safety layer
* Query explanation in business terms
* Interactive dashboard (Streamlit)

---

## 🏗️ Architecture

User Query → LLM → SQL → Validator → Database → Results → Explanation

---

## 🛠️ Tech Stack

* Python (FastAPI)
* OpenAI / Gemini API
* SQLite (mock database)
* Streamlit UI

---

## 📊 Sample Use Cases

* Business analytics queries
* Revenue insights
* Customer segmentation

---

## ⚙️ Setup

```bash
git clone https://github.com/yourusername/DataCopilot.git
cd DataCopilot
pip install -r requirements.txt
```

Run backend:

```bash
uvicorn app.main:app --reload
```

Run UI:

```bash
streamlit run ui/streamlit_app.py
```

---

## 📈 Future Improvements

* Query accuracy evaluation
* Role-based access control
* Multi-database support
* Query correction loop

---


