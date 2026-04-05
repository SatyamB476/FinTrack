from decimal import Decimal
import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="satyam391",
        database="fintrack_db"
    )
    return conn

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