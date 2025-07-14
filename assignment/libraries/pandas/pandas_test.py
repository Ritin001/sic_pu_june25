import pandas as pd

#reading the values of the excel
df = pd.read_excel("C:\\Users\\RITIN\\Desktop\\unemployment data.xlsx")
#print(df.count())
print(df.head(5))
print(df.tail(5))


