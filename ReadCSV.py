import pandas as pd
import numpy as np

obj = pd.read_csv("nyc_weather.csv")
#print(obj)

# Write the DataFrame to an excel file

#obj.to_excel('Expense.xlsx')
for index, row in obj.iterrows():
    print(index, row.EST)
