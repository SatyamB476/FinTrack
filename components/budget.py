import streamlit as st
from db.queries import add_budget, get_budgets, get_budget_vs_actual
import pandas as pd
import plotly.express as px

def show_budget():
    st.subheader("🎯 Set Monthly Budget")

    col1, col2 = st.columns(2)

    with col1:
        category = st.selectbox("Category", [
            "Food", "Transport", "Shopping", "Entertainment",
            "Health", "Education", "Rent", "Other"
        ])
        monthly_limit = st.number_input("Monthly Limit (₹)", min_value=0.0, format="%.2f")

    with col2:
        month = st.text_input("Month (YYYY-MM)", placeholder="2025-04")

    if st.button("Set Budget"):
        if monthly_limit == 0.0 or month == "":
            st.warning("Please fill all fields.")
        else:
            add_budget(category, monthly_limit, month)
            st.success(f"Budget set for {category} - {month}")

    st.divider()

    st.subheader("📊 Budget vs Actual Spending")

    compare_month = st.text_input("Enter Month to Compare (YYYY-MM)", placeholder="2026-04")

    if st.button("Compare"):
        if compare_month == "":
            st.warning("Please enter a month.")
        else:
            data = get_budget_vs_actual(compare_month)
            if data:
                df = pd.DataFrame(data)
                df.columns = df.columns.str.lower()
                for col in ("monthly_limit", "actual_spent"):
                    df[col] = pd.to_numeric(df[col], errors="coerce").astype(float)

                st.write(df)  # debug: remove after confirming chart values

                chart_df = df.melt(
                    id_vars="category",
                    value_vars=["monthly_limit", "actual_spent"],
                    var_name="type",
                    value_name="amount",
                )
                fig = px.bar(
                    chart_df,
                    x="category",
                    y="amount",
                    color="type",
                    barmode="group",
                    title=f"Budget vs Actual - {compare_month}",
                    labels={"amount": "Amount (₹)", "type": "Type", "category": "Category"},
                    color_discrete_map={
                        "monthly_limit": "#2ecc71",
                        "actual_spent": "#e74c3c",
                    },
                )
                st.plotly_chart(fig, use_container_width=True)

                # Overspent alert
                st.subheader("⚠️ Overspent Categories")
                overspent = df[df['actual_spent'] > df['monthly_limit']]
                if not overspent.empty:
                    for _, row in overspent.iterrows():
                        st.error(f"🚨 {row['category']} — Limit: ₹{row['monthly_limit']} | Spent: ₹{row['actual_spent']}")
                else:
                    st.success("✅ You are within budget for all categories!")

            else:
                st.info("No budgets found for this month. Set budgets first.")

    st.divider()

    st.subheader("📋 View Budgets")
    view_month = st.text_input("Enter Month to View (YYYY-MM)", placeholder="2026-04")
    if st.button("View"):
        data = get_budgets(view_month)
        if data:
            df = pd.DataFrame(data)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No budgets found for this month.")