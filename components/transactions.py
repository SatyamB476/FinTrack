import streamlit as st
from db.queries import add_transaction, get_all_transactions, delete_transaction
import pandas as pd

def show_transactions():
    st.subheader("➕ Add Transaction")

    col1, col2 = st.columns(2)

    with col1:
        date = st.date_input("Date")
        category = st.selectbox("Category", [
            "Food", "Transport", "Shopping", "Entertainment",
            "Health", "Education", "Rent", "Salary", "Other"
        ])
        type_ = st.radio("Type", ["income", "expense"])

    with col2:
        amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f")
        description = st.text_input("Description")

    if st.button("Add Transaction"):
        if amount == 0.0:
            st.warning("Please enter a valid amount.")
        else:
            add_transaction(date, category, amount, type_, description)
            st.success("Transaction added successfully!")

    st.subheader("📋 All Transactions")

    data = get_all_transactions()

    if data:
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)

        st.subheader("🗑️ Delete Transaction")
        delete_id = st.number_input("Enter Transaction ID to delete", min_value=1, step=1)
        if st.button("Delete"):
            delete_transaction(delete_id)
            st.success(f"Transaction {delete_id} deleted.")
    else:
        st.info("No transactions found. Add one above!")