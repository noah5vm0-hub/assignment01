import sqlite3

# 連接資料庫（若不存在會自動建立）
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# 建立資料表
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    notes TEXT
)
""")

# 使用者輸入
date = input("Enter date (YYYY-MM-DD): ")
amount = float(input("Enter amount: "))
category = input("Enter category (e.g. Food, Transport): ")
notes = input("Enter notes (optional): ")

# 新增資料
cursor.execute("""
INSERT INTO expenses (date, amount, category, notes)
VALUES (?, ?, ?, ?)
""", (date, amount, category, notes))

conn.commit()
conn.close()

print("✅ Expense saved successfully!")
