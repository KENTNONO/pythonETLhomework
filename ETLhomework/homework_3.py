##練習使用pandas 發覺沒有很難就繼續做了

import pandas as pd
df = pd.DataFrame(columns=['Name','Age','Height'])
df.loc[0] = ['Allen','22','175']
print(df)
df.to_csv(r'./test_pandas1.csv',index=False,encoding='utf-8')