import os
import pandas as pd
from groq import Groq
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY", None)
client = Groq(api_key=groq_api_key)

def get_ai_insights(df):
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    total_income = df[df['type'] == 'income']['amount'].sum()
    total_expense = df[df['type'] == 'expense']['amount'].sum()
    balance = total_income - total_expense
    top_categories = df[df['type'] == 'expense'].groupby('category')['amount'].sum().nlargest(3).to_dict()

    prompt = f"""
    You are a personal finance advisor. Analyze this user's spending data and give smart insights:
    - Total Income: ₹{total_income}
    - Total Expense: ₹{total_expense}
    - Balance: ₹{balance}
    - Top Spending Categories: {top_categories}
    Give:
    1. Overall financial health summary
    2. Spending pattern observations
    3. 3 actionable saving tips
    Keep it short, friendly and practical.
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
