import pandas as pd
biz_file_path = "C:\\Users\\Asus\\OneDrive\\Documents\\Tarun docs\\Business_data.csv"
biz_data = pd.read_csv(biz_file_path)
print(biz_data.describe())

print(biz_data.columns)

y = biz_data.Period

biz_features = ['Period','Data_value', 'Suppressed', 'STATUS','UNITS', 'Magnitude', 'Subject', 'Group',]
x = biz_data[biz_features]

print(x.describe())
print(x.head())
