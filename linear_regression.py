import pandas as pd
import pickle 


data = pd.read_csv("H:/flask/linear-regression.csv")
data = data.fillna(value=25)

x = data.drop('price', axis=1)
y = data.price
from sklearn.linear_model import LinearRegression

obj = LinearRegression()

obj.fit(x, y)

pickle.dump(obj, open("model.pkl", "wb"))