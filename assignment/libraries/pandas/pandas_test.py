import pandas as pd

#reading the values of the excel
df = pd.read_excel("C:\\Users\\RITIN\\Desktop\\unemployment data.xlsx")
#print(df.count())
print(df.head(5))
print(df.tail(5))


df.info()  #type of coloumns
df.shape  #COUNT THE ROWS
df.drop(['indicator_name'],axis = 1) #drop the indicator name row but temp, if we write df.drop(['indicator_name'],axis = 1,inpace=True) it will delete permanantly , axis 1 = coloumns axis 0 = rows
#df['sex'] = df['sex'].map(('Female':0,'male':1)) # replace th values with 0 and 1   
