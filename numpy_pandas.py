
import pandas as pd
import numpy as np

data = [[1, 'A', 5], [2, 'B', 6], [3, 'C', 7], [4, 'D', 8], [5, 'E', 9],
        [6, 'F', 10], [7, 'G', 11], [8, 'H', 12], [9, 'I', 13], [10, 'J', 14]]
df = pd.DataFrame(data, columns=['ID', 'Letter', 'Value'])
print("Original DataFrame:")
print(df)

filtered_df_1 = df[df['Value'] > 10]
print("\nFiltered DataFrame (Value > 10):")
print(filtered_df_1)

filtered_df_2 = df[(df['Value'] > 8) & (df['Letter'] == 'C')]
print("\nFiltered DataFrame (Value > 8 and Letter == 'C'):")
print(filtered_df_2)

df['Letter'] = df['Letter'].replace('A', 'Z')
print("\nDataFrame after replacing 'A' with 'Z' in 'Letter' column:")
print(df)

df2 = pd.DataFrame(np.random.randint(1, 20, size=(10, 3)), columns=['ID', 'Letter', 'Value'])
print("\nSecond DataFrame (df2) with random data:")
print(df2)


appended_df = pd.concat([df, df2], ignore_index=True)
print("\nAppended DataFrame:")
print(appended_df)
