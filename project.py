import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

print(df.head())
print(df.info())
print(df.describe())

# Sales chart
df.hist(figsize=(10,8))
plt.show()
