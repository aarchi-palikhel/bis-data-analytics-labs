import os
import pandas as pd
import sqlalchemy as sq
import urllib

# Define database connection parameters
server_name = "DESKTOP-6HBTVKU"
database_name = "BIS"
directory_path = "D:\\Aarchi_022bim003\\Lab_4"

# Define the connection string using urllib to encode parameters
params = urllib.parse.quote_plus(
    "Driver={ODBC Driver 17 for SQL Server};"
    f"Server={server_name};"
    f"Database={database_name};"
    "Trusted_Connection=yes;"
)
connection_string = f"mssql+pyodbc:///?odbc_connect={params}"

# Create SQLAlchemy engine
try:
    engine = sq.create_engine(connection_string, echo=False)
    # Test the connection
    engine.connect()
    print("==========================")
    print("CONNECTION SUCCESSFUL")
    print("==========================")
except Exception as e:
    print("Database connection failed:", e)
    exit()

# Process all files in the specified directory
try:
    for file_name in os.listdir(directory_path):
        if file_name.endswith('.csv') or file_name.endswith('.xlsx'):
            file_path = os.path.join(directory_path, file_name)
            print(f"Importing file: {file_path}")

            # Read the file into a Pandas DataFrame
            if file_name.endswith('.csv'):
                df = pd.read_csv(file_path, dtype=str)
            else:  # file_name.endswith('.xlsx')
                df = pd.read_excel(file_path, dtype=str)

            # Clean the DataFrame (replace commas in data)
            df = df.replace(",", "", regex=True)

            # Log basic information
            print(f"Number of records: {len(df)}")
            print("First few rows:")
            print(df.head())

            # Use the file name (without extension) as the table name
            table_name = os.path.splitext(file_name)[0]

            # Upload the DataFrame to the SQL Server table
            df.to_sql(table_name, engine, index=False, if_exists='append')
            print(f"File {file_name} imported successfully into table '{table_name}'.")
except Exception as e:
    print("Error during file import:", e)

print("==========================")
print("FILES IMPORTED SUCCESSFULLY")
print("==========================")