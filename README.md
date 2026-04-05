# 💰 FinTrack - Personal Finance Tracker

A data analytics web application for tracking personal income and expenses, built with Python, Streamlit, MySQL, and AI-powered insights using Groq API.

---

## 🚀 Features

- **Transaction Management** — Add, view, and delete income/expense transactions stored in MySQL
- **Finance Dashboard** — Interactive charts showing category breakdown, monthly trends, and daily spending
- **AI Financial Insights** — LLaMA 3.3 70B powered analysis of spending patterns with personalized saving tips

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Database | MySQL |
| Data Processing | Python, Pandas |
| Visualizations | Plotly |
| AI Insights | Groq API (LLaMA 3.3 70B) |

---
## 📁 Project Structure

    fintrack/
    ├── app.py                    
    ├── db/
    │   └── queries.py            
    ├── components/
    │   ├── dashboard.py          
    │   └── transactions.py       
    ├── ai/
    │   └── insights.py           
    ├── .gitignore
    └── requirements.txt

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

    DB_HOST=localhost
    DB_USER=your_mysql_user
    DB_PASSWORD=your_mysql_password
    DB_NAME=fintrack_db
    GROQ_API_KEY=your_groq_api_key

**4. Create MySQL database**
```sql
CREATE DATABASE fintrack_db;
USE fintrack_db;

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    category VARCHAR(50),
    amount DECIMAL(10,2),
    type ENUM('income', 'expense'),
    description VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**5. Run the app**
```bash
streamlit run app.py
```

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

**Satyam** — Final Year B.Tech Computer Science
GitHub: [SatyamB476](https://github.com/SatyamB476)
