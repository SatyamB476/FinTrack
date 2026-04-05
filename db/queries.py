from decimal import Decimal

from db.connection import get_connection


def _row_to_plain_dict(row):
    """Lowercase keys and convert MySQL DECIMAL to float for pandas/plotly."""
    out = {}
    for key, value in row.items():
        k = key.lower() if isinstance(key, str) else key
        if isinstance(value, Decimal):
            out[k] = float(value)
        else:
            out[k] = value
    return out

# ── TRANSACTIONS ──

def add_transaction(date, category, amount, type_, description):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO transactions (date, category, amount, type, description)
        VALUES (%s, %s, %s, %s, %s)
    """, (date, category, amount, type_, description))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_transactions():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def delete_transaction(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

# ── BUDGETS ──

def add_budget(category, monthly_limit, month):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO budgets (category, monthly_limit, month)
        VALUES (%s, %s, %s)
    """, (category, monthly_limit, month))
    conn.commit()
    cursor.close()
    conn.close()

def get_budgets(month):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM budgets WHERE month = %s", (month,))
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def get_budget_vs_actual(month):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT 
            b.category,
            b.monthly_limit,
            COALESCE(SUM(t.amount), 0) AS actual_spent
        FROM budgets b
        LEFT JOIN transactions t 
            ON b.category = t.category 
            AND t.type = 'expense'
            AND YEAR(t.date) = YEAR(STR_TO_DATE(%s, '%%Y-%%m'))
            AND MONTH(t.date) = MONTH(STR_TO_DATE(%s, '%%Y-%%m'))
        WHERE b.month = %s
        GROUP BY b.category, b.monthly_limit
    """, (month, month, month))
    data = [_row_to_plain_dict(r) for r in cursor.fetchall()]
    cursor.close()
    conn.close()
    return data