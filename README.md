# 💰 FinTrack - Personal Finance Tracker

> A personal finance web application for tracking income and expenses with AI-powered insights — built with Python, Streamlit, SQLite, and Groq API.

---

## 🔴 Live Demo

**[https://fintrack-j7dsndlef5vbzmyuzkkddh.streamlit.app/](https://fintrack-j7dsndlef5vbzmyuzkkddh.streamlit.app/)**

---

## 🚀 Features

- **Transaction Management** — Add, view, and delete income/expense transactions stored in SQLite
- **Finance Dashboard** — Interactive charts showing category breakdown, monthly trends, and daily spending
- **AI Financial Insights** — LLaMA 3.3 70B powered analysis of spending patterns with personalized saving tips

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Database | SQLite |
| Data Processing | Python, Pandas |
| Visualizations | Plotly |
| AI Insights | Groq API (LLaMA 3.3 70B) |

---

## 📁 Project Structure

```
FinTrack/
├── app.py                    # Main Streamlit app
├── db/
│   └── queries.py            # SQLite DB operations
├── components/
│   ├── dashboard.py          # Dashboard charts
│   └── transactions.py       # Transaction management UI
├── ai/
│   └── insights.py           # Groq AI insights
├── .gitignore
└── requirements.txt
```

---

## ⚙️ Setup & Installation

**1. Clone the repository**
```bash
git clone https://github.com/SatyamB476/FinTrack.git
cd FinTrack
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Create `.env` file**
```
GROQ_API_KEY=your_groq_api_key
```
Get your free API key at [console.groq.com](https://console.groq.com)

**4. Run the app**
```bash
streamlit run app.py
```

> SQLite database is created automatically on first run — no setup needed.

---

## 📊 Dashboard Features

- **Expense by Category** — Pie chart breakdown of spending
- **Monthly Income vs Expense** — Grouped bar chart trend
- **Daily Expense Trend** — Line chart for day-wise spending
- **Key Metrics** — Total Income, Total Expense, Balance

---

## 🤖 AI Insights

Powered by Groq API with LLaMA 3.3 70B model. Analyzes real transaction data and provides:
- Overall financial health summary
- Spending pattern observations
- 3 actionable saving tips

---

## 👨‍💻 Author

**Satyam** — Final Year Computer Science
GitHub: [SatyamB476](https://github.com/SatyamB476)
