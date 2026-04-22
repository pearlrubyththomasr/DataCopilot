# 🤖 DataCopilot – AI-Powered Natural Language to SQL Assistant

## 🚀 Overview

DataCopilot is an AI-driven system that allows users to query structured data using natural language.
Instead of writing SQL, users can ask questions like:

> “Show top 5 customers by revenue”

The system generates SQL, executes it on a database, and returns results along with business-friendly explanations and visual insights.

---

## 🧠 Key Features

### 🔹 Natural Language → SQL

* Converts user queries into SQL using a local LLM (Ollama)
* Schema-aware query generation
* Supports joins, aggregations, and filtering

### 🔹 Self-Healing Query System

* Detects SQL execution errors
* Automatically corrects queries using LLM feedback
* Retries execution without user intervention

### 🔹 Explainability Layer

* Converts SQL queries into simple business explanations
* Makes insights accessible to non-technical users

### 🔹 Interactive Dashboard

* Built using Streamlit
* Displays:

  * Generated SQL
  * Query results
  * KPI metrics
  * Charts (Plotly)

### 🔹 Dynamic CSV Upload (New 🚀)

* Users can upload their own datasets
* System dynamically generates schema from uploaded data
* Queries work on custom datasets without code changes

---

## 🏗️ Architecture

User Query → LLM → SQL → Validator → Database → Results → Explanation → Dashboard

---

## 🛠️ Tech Stack

* **Python**
* **SQLite** (database)
* **Streamlit** (UI)
* **Ollama (Mistral)** – local LLM
* **Pandas** – data processing
* **Plotly** – visualization

---

## 📂 Project Structure

```
DataCopilot/
│
├── app/
│   ├── llm.py               # NL → SQL + self-healing
│   ├── db.py                # Database execution layer
│   ├── pipeline.py          # End-to-end query pipeline
│   ├── validator.py         # SQL safety checks
│   ├── explainability.py    # SQL → business explanation
│   └── main.py              # Backend entry point (future use)
│
├── ui/
│   └── streamlit_app.py     # Dashboard UI
│
├── data/
│   ├── sap_mock.db
│   └── sample datasets
│
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/DataCopilot.git
cd DataCopilot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Ollama (Local LLM)

```bash
ollama run mistral
```

### 4. Start Application

```bash
streamlit run ui/streamlit_app.py
```

---

## 📊 Example Queries

* Show total revenue by region
* Top 5 customers by revenue
* Total revenue by product
* Which region generates the highest revenue?

---

## 🧪 Example Workflow

1. Upload a CSV dataset (optional)
2. Ask a question in natural language
3. System:

   * Generates SQL
   * Executes query
   * Fixes errors (if any)
   * Displays results + explanation + charts

---

## ⚠️ Known Limitations

* CSV parsing may fail for malformed files (will be improved)
* LLM accuracy depends on schema clarity
* Local LLM may be slower than cloud APIs

---

## 🚀 Future Improvements

* Robust CSV cleaning & validation
* Multi-table support
* Role-based access control
* Query history persistence
* Support for multiple databases

---

## 💡 Key Learnings

* Integrating LLMs with structured data systems
* Handling SQL dialect mismatches
* Building self-healing pipelines using feedback loops
* Designing explainable AI systems for business users

---


---
