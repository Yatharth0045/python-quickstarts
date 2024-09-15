import pandas as pd

# Sample data in the form of a dictionary
# data = {
#     "User ID": [1234, 2345],
#     "Aadhar": ["XXXX-XXXX-5566", "XXXX-XXXX-7788"],
#     "Amount": [5000, 6000],
#     "Status": ["Failed", "Failed"],
#     "Response Code": ["U16", "U3"],
#     "Response Message": ["Risk Threshold", "Fingerprint Mismatch"],
#     "Date & Time": ["10-07-24 12:09", "10-07-24 12:09"]
# }

# Create a DataFrame
df = pd.read_excel('sheet.xlsx', sheet_name='Sheet1')
# df = pd.DataFrame(data)

# Define a function to check the conditions
def check_conditions(df):
    # Initial flags
    df['Flag'] = 'None'

    # Check each condition
    for user_id in df['User ID'].unique():
        user_df = df[df['User ID'] == user_id]
        count_U16 = len(user_df[user_df['Response Code'] == 'U16'])
        count_U3 = len(user_df[user_df['Response Code'] == 'U3'])
        total_transactions = len(user_df)
        failed_transactions = len(user_df[user_df['Status'] == 'Failed'])
        
        # Condition 1
        if count_U16 > 0:
            df.loc[df['User ID'] == user_id, 'Flag'] = 'Yellow'

        # Condition 2
        if count_U3 > 0:
            df.loc[df['User ID'] == user_id, 'Flag'] = 'Yellow'
        
        # Condition 3
        if total_transactions > 0:
            df.loc[df['User ID'] == user_id, 'Flag'] = 'Yellow'

        # Condition 4
        if count_U16 > 0 and count_U3 > 0 and total_transactions > 0:
            df.loc[df['User ID'] == user_id, 'Flag'] = 'Red'

    return df

# Apply the function
df = check_conditions(df)

df.to_excel('sheet.xlsx', index=False, sheet_name='Sheet1')

# Print the DataFrame to check the flags
print(df)
