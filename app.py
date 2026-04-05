import streamlit as st
from components.transactions import show_transactions
from components.dashboard import show_dashboard
from ai.insights import get_ai_insights
from db.queries import get_all_transactions, init_db
import pandas as pd

# Initialize DB on startup
init_db()

st.set_page_config(
    page_title="FinTrack - Personal Finance Tracker",
    page_icon="💰",
    layout="wide"
)

st.title("💰 FinTrack - Personal Finance Tracker")

menu = st.sidebar.radio("Navigation", [
    "Dashboard",
    "Transactions",
    "AI Insights"
])

if menu == "Dashboard":
    show_dashboard()
elif menu == "Transactions":
    show_transactions()
elif menu == "AI Insights":
    st.subheader("🤖 AI Financial Insights")
    data = get_all_transactions()
    if data:
        df = pd.DataFrame(data)
        with st.spinner("Analyzing your finances..."):
            insights = get_ai_insights(df)
        st.markdown(insights)
    else:
        st.info("Add some transactions first to get AI insights!")
