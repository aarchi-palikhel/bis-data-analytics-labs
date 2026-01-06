import pandas as pd
from sqlalchemy import create_engine

# Step 1: Read Excel
file_path = "D:\\Aarchi_022bim003\\Monthly_statistics.xlsx"
df = pd.read_excel(file_path, engine='openpyxl')

# Step 2: Clean (if needed)
df.dropna(how='all', inplace=True)
df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace(r'[^\w]', '', regex=True)

# Step 3: Connect to SQL Server
server = "DESKTOP-6HBTVKU"
database = "Aarchi"
table_name = "Monthly_statistics"

# Windows Auth
conn_str = f"mssql+pyodbc://@{server}/{database}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(conn_str)

# Step 4: Upload to SQL
df.to_sql(table_name, con=engine, if_exists='replace', index=False)

print("✅ Excel file uploaded to SQL Server.")
