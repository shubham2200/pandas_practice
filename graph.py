import pandas as pd
import matplotlib.pyplot as plt

data = {
    'CITY':['mumbai' , 'pune' , 'kolhapur' , 'nashik' , 'nanded' , 'jalgaon'],
    'IT COMPANYS':[23 , 45 , 9 , 18 , 3  , 6]
}
df = pd.DataFrame(data,columns=['CITY','IT COMPANYS'])
df.plot(x ='CITY', y='IT COMPANYS', kind = 'bar')
plt.show(df)