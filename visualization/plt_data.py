#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd


# read csv
df = pd.read_csv('electronic-card-transactions-september-2020-csv-tables.csv')

# statistics regarding values in numeric columns
df.describe()

# information about columns and values
df.info(verbose=True)

# removing of columns that contain only nulls
df = df.dropna(axis=1,how='all')

# change column type
df['Period'] = df['Period'].astype(str)

# grouping with filter on string column
df_grouped = df[df['Period'].str.contains("2020.")].groupby(['Period']).sum()

# pie plot
plot = df_grouped.plot.pie(x='Period',y='Data_value', figsize=(5, 5))

# show plot
plt.show()