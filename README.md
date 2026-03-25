# Neohive---Bug-slayerz-project
# 💰 Budget Planner AI Agent

An AI-powered tool that generates a structured monthly budget plan based on user income and expenses.

---

## 🚀 Features

* Calculates total expenses and savings
* Provides categorized expense breakdown
* Generates smart financial recommendations
* Uses **Pydantic** for structured output validation

---

## 🏗️ Tech Stack

* Python
* OpenRouter API (LLM)
* Pydantic

---

## ⚙️ Setup

```bash
git clone https://github.com/VDevanarayanan/Neohive---Bug-slayerz-project.git
cd budget_planner

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

## ▶️ Run

```bash
python budget_planner/main.py
```

---

## 🧠 How It Works

1. Takes user input (income + expenses)
2. Sends prompt to LLM via OpenRouter
3. Extracts JSON from response
4. Validates using Pydantic
5. Outputs clean budget plan

---

