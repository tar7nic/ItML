import pandas as pd 

data_path = "C:\\Users\\Asus\\OneDrive\\Documents\\Tarun docs\\Book1.xlsx"
data = pd.read_excel(data_path)

print(data.head())
data_features = ['Size', 'Wt.','Qty','Unit']
X = data[data_features]
y = data.Qty
print(X.describe())

from sklearn.tree import DecisionTreeRegressor
data_model = DecisionTreeRegressor(random_state=1)
print(data_model.fit(X,y))

# def HelloWorld(str):
#     print(str)
    
# HelloWorld("print")
# HelloWorld("Jit pagal hai")