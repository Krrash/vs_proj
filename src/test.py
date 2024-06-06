#libraries
import pandas as pd
import numpy as np

#create second csv
# df2 = pd.DataFrame({
#     'seq': range(1000),
#     'performance_score': np.random.randint(1, 10, size=1000),
#     'salary': np.random.randint(30000, 100000, size=1000)
# })

#create csv
#df2.to_csv('csv2.csv', index=False)

# Read CSV files
df1 = pd.read_csv('csv1.csv')
df2 = pd.read_csv('csv2.csv')

# Merge DataFrames
merged_df = pd.merge(df1, df2, on='id')

# Select specific columns
merged_df = merged_df[['id', 'name/first', 'age', 'city', 'state', 'salary', 'performance_score']]

# Change data type
merged_df['age'] = merged_df['age'].astype(float)

# Remove duplicates
merged_df = merged_df.drop_duplicates(subset=['name/first'])

# Reshape DataFrame (melt)
melted_df = pd.melt(merged_df, id_vars=['id'], value_vars=['salary', 'performance_score'])


# Load the DataFrame into a MySQL table using SQLAlchemy
from sqlalchemy import create_engine, text


# Create an engine and connect to MySQL
engine = create_engine('mysql+pymysql://root:kaushal@localhost:3306/EmpData')

with engine.connect() as connect:

# # Load the merged DataFrame into the new MySQL database
    merged_df.to_sql(name='employee_imported', con=connect, if_exists='replace', index=False)
    print(merged_df)
    print(connect.closed)
    connect.close()

