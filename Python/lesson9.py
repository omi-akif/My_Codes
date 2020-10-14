import pandas as pd
city = ['dhaka', 'chattagram', 'barishal', 'rangpur']
ser1 = pd.Series(city)
print (ser1)
ser2=pd.Series([1,2,5,6,8])
print(ser2)
lab=['a','b','c','d']
ser3 = pd.Series(data=city, index=lab)
print(ser3)
city2={'a':'dhaka','b':'chattagram'}
print(city2)
ser5=pd.Series(city2)
print(ser5)
print(ser5.values)
print(ser5.index)