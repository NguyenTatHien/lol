import numpy as np 
import pandas
df = pandas.read_excel('C:\\CODE\\Toán rời rạc\\Chuong5_23_06_2022\\monhoc.xlsx') 
print (df.columns) # liệt kê các cột dữ liệu 
giatri = df['Thể dục'].values # đọc 1 cột dữ liệu
print(giatri)