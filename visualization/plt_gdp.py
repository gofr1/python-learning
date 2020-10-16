#!/usr/bin/env python3
#pip install xlrd

import matplotlib.pyplot as plt
import pandas as pd


# read Excel file
df = pd.read_excel('Download-GDPPC-USD-countries.xlsx', header = 2)

# sort and select top 20
df = df.sort_values(by=2018, ascending = False).head(20)

# plot!
ax = df.plot.bar(x="Country", y=2018, color="red", align="center")
ax.set_title('Per Capita GDP at current prices in US Dollars (all countries)')
plt.show()