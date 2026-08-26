import pandas as pd

# Load the CSV files
file1 = 'C:\\dev\\tmp\\a.csv'
file2 = 'C:\\dev\\tmp\\b.csv'

# Read the CSV files into DataFrames
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Specify the columns to match on, e.g., ['ID', 'Name']
merge_columns = ['rulename', 'appname']

# Merge the DataFrames on the specified columns
merged_df = pd.merge(df1, df2, on=merge_columns, how='outer', suffixes=('_file1', '_file2'))

# List of columns to update totals for
total_columns = ['sumsent','sumrecieved']

# Combine the totals for specified columns
for column in total_columns:
    merged_df[column] = merged_df[[f"{column}_file1", f"{column}_file2"]].sum(axis=1)
    merged_df.drop([f"{column}_file1", f"{column}_file2"], axis=1, inplace=True)

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('C:\\dev\\tmp\\merged_output.csv', index=False)

print("CSV files have been successfully merged and totals updated!")
