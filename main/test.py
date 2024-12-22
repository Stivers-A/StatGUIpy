import pandas as pd

df = pd.DataFrame({'A': [1, 2], 'B': ['string', 4]})

# Create a list from the first row
row_list = df.iloc[0].tolist()

print(row_list)