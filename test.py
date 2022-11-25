import pandas as pd


chunk = pd.read_csv('G:\Python projects\Ofogh_Kurosh\data\Filtered data/Example.csv', chunksize=1000)
df = pd.concat(chunk)
ali = pd.DataFrame(df.groupby(by='TRANSACTIONID')['Information'])
print(ali.value_counts())