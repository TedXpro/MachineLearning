import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv("crop_yield.csv")
data = data.dropna(axis=0)

print(data.head())