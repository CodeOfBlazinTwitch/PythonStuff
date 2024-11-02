import pandas as pd
print(pd.__version__)
print("hi")

data = pd.Series([0.25, 0.5, 0.75, 1.0])
print("data: \n", data)
print("values: \n", data.values)
print("index: \n", data.index)
print("keys: \n", data.keys)

data2 = pd.Series([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print("describe: \n", data2.describe())
print("agg: \n", data2.agg(["mean", "std", "min", "max"]))

hi