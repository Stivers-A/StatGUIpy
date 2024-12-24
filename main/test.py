# importing pandas as pd
import pandas as pd

# Create the dataframe
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/11'],
                   'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
                   'Cost':[10000, 5000, 15000, 2000]})

# Print the dataframe
print(df, " dataframe")
# Create an empty list
Row_list =  df.T



# Print the list
print(Row_list )