import pandas as pd

df = pd.read_csv(r'C:\Users\USER\Desktop\class\FEB-2025-PYTHON-SESSIONS\Week 6A\Week 7\sales_data.csv')
df['revenue'] = df['quantity'] * df['price']
total_revenue = df['revenue'].sum()

best_selling_product = df.groupby('product')['quantity'].sum().idxmax()

highest_sales_day = df.groupby('date')['revenue'].sum().idxmax()

with open('sales_summary.txt', 'w') as file:
    file.write(f"Total Revenue: ${total_revenue:.2f}\n")
    file.write(f"Best-Selling Product: {best_selling_product}\n")
    file.write(f"Day with Highest Sales: {highest_sales_day}\n")

print(df.columns)
print("Sales Summary:")
print(f"Total Revenue: ${total_revenue:.2f}")
print(f"Best-Selling Product: {best_selling_product}")
print(f"Day with Highest Sales: {highest_sales_day}")

