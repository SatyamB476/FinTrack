import streamlit as st
import pandas as pd
import plotly.express as px
from db.queries import get_all_transactions

def show_dashboard():
    st.subheader("📊 Finance Dashboard")

    data = get_all_transactions()

    if not data:
        st.info("No transactions found. Add some transactions first!")
        return

    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.strftime('%Y-%m')

    # ── OVERVIEW METRICS ──
    total_income = df[df['type'] == 'income']['amount'].sum()
    total_expense = df[df['type'] == 'expense']['amount'].sum()
    balance = total_income - total_expense

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Income", f"₹{total_income:,.2f}")
    col2.metric("Total Expense", f"₹{total_expense:,.2f}")
    col3.metric("Balance", f"₹{balance:,.2f}")

    st.divider()

    # ── CATEGORY WISE EXPENSE ──
    st.subheader("💸 Expense by Category")
    expense_df = df[df['type'] == 'expense']
    if not expense_df.empty:
        cat_df = expense_df.groupby('category')['amount'].sum().reset_index()
        fig1 = px.pie(cat_df, names='category', values='amount', title="Category Breakdown")
        st.plotly_chart(fig1, use_container_width=True)

    # ── MONTHLY TREND ──
    st.subheader("📈 Monthly Income vs Expense")
    monthly_df = df.groupby(['month', 'type'])['amount'].sum().reset_index()
    fig2 = px.bar(monthly_df, x='month', y='amount', color='type',
              barmode='group', title="Monthly Trend",
              color_discrete_map={'income': '#2ecc71', 'expense': '#e74c3c'},
              category_orders={'type': ['income', 'expense']})
    st.plotly_chart(fig2, use_container_width=True)

    # ── DAY WISE SPENDING ──
    st.subheader("📅 Day-wise Spending")
    daily_df = df[df['type'] == 'expense'].groupby('date')['amount'].sum().reset_index()
    fig3 = px.line(daily_df, x='date', y='amount', title="Daily Expense Trend")
    st.plotly_chart(fig3, use_container_width=True)