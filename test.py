import pandas as pd

# Load the two Excel files into DataFrames
file1 = "PS_BI_HDR_LAGO(in).xlsx"
file2 = "PS_BI_HDR_PEOPLE(in).xlsx"

# Read the Excel files
df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

print(f"File 1 shape: {df1.shape}")
print(f"File 2 shape: {df2.shape}")

print(df1.head())
print(df2.head())   

# Create a list to store differences
differences = []

# Get common columns between both DataFrames
common_columns = df1.columns.intersection(df2.columns)

# Compare each cell and store differences
for col in common_columns:
    # Compare each cell in the column
    mask = df1[col] != df2[col]
    for idx in mask[mask].index:
        differences.append({
            'Row_Number': idx,
            'Column_Name': col,
            'LAGO_Value': str(df1.loc[idx, col]),
            'PEOPLE_Value': str(df2.loc[idx, col])
        })

# Create and save differences report
if differences:
    output_file = 'differences_report.txt'
    with open(output_file, 'w') as f:
        f.write("Differences Report between LAGO and PEOPLE files\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Total differences found: {len(differences)}\n\n")
        
        for diff in differences:
            f.write(f"Row Number: {diff['Row_Number']}\n")
            f.write(f"Column Name: {diff['Column_Name']}\n")
            f.write(f"LAGO Value: {diff['LAGO_Value']}\n")
            f.write(f"PEOPLE Value: {diff['PEOPLE_Value']}\n")
            f.write("-" * 50 + "\n\n")
    
    print(f"Total differences found: {len(differences)}")
    print(f"Differences have been saved to {output_file}")
else:
    print("\nNo differences found - the files are identical.")