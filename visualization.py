import sqlite3
import matplotlib.pyplot as plt

#連接資料庫
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

#依類別統計金額
cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
""")

data = cursor.fetchall()
conn.close()

#拆解資料
categories = [row[0] for row in data]
amounts = [row[1] for row in data]

#繪製圓餅圖
plt.figure()
plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
plt.title("Expense Distribution by Category")
plt.axis("equal")  # 讓圓形比例正常
plt.show()