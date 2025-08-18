import pandas as pd
import sqlite3

# Load Excel files
food_df = pd.read_excel("zomato food.xlsx", sheet_name="food")
menu_df = pd.read_excel("zomato menu.xlsx", sheet_name="menu")
menu_df = menu_df.drop_duplicates()
orders_df = pd.read_excel("zomato orders.xlsx", sheet_name="orders")
restaurant_df = pd.read_excel("zomato restaurant.xlsx", sheet_name="restaurant")
users_df = pd.read_excel("zomato users.xlsx", sheet_name="users")

# Create SQLite DB
conn = sqlite3.connect("zomato.db")

# Save each dataframe as a table
food_df.to_sql("food", conn, if_exists="replace", index=False)
menu_df.to_sql("menu", conn, if_exists="replace", index=False)
orders_df.to_sql("orders", conn, if_exists="replace", index=False)
restaurant_df.to_sql("restaurant", conn, if_exists="replace", index=False)
users_df.to_sql("users", conn, if_exists="replace", index=False)

print("✅ SQLite database 'zomato.db' created successfully!")

# Optional: Show tables
tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
print("📋 Tables in DB:", tables)

conn.close()
