# import required modules
import pandas as pd
import numpy as np
from datetime import datetime as dt


def hour_remover(string1):
    date_format = '%m/%d/%Y'
    try:
        return dt.strptime(string1.split(' ')[0], date_format)
    except:
        print('Error')

chunk = pd.read_csv('G:\Python projects\Ofogh_Kurosh\data\Filtered data/RFM_data.csv', chunksize=1000)
df = pd.concat(chunk)
df['TRANSDATE'] = df['TRANSDATE'].map(hour_remover)

df_recency = pd.DataFrame(df.groupby(by='Information', as_index=False)['TRANSDATE'].max())
recent_date = df_recency['TRANSDATE'].max()
df_recency['Recency'] = df_recency['TRANSDATE'].map(lambda x: (recent_date - x).days)
df_recency.drop(columns='TRANSDATE', inplace=True)

df_frequency = pd.DataFrame(df.groupby(by='Information', as_index=False)['TRANSDATE'].count())
df_monetary = pd.DataFrame(df.groupby(by='Information', as_index=False)['NetAmount'].sum())

df_RFM = df_recency
df_RFM['Frequency'] = df_frequency['TRANSDATE']
df_RFM['Monetary'] = df_monetary['NetAmount']
df_RFM.to_csv('G:\Python projects\Ofogh_Kurosh\data\Filtered data/processed_RFM_data.csv')
# num_of_money_clusters = 5
# money_clusters_step = (df['NETAMOUNT'].max() - df['NETAMOUNT'].min()) / num_of_money_clusters
# df['money_clusters'] = df['NETAMOUNT']
#
# df_gb1 = pd.DataFrame(df.groupby(by='TRANSACTIONID')['NETAMOUNT'].sum())
# df_gb2 = pd.DataFrame(df.groupby(by='TRANSACTIONID')['Information', 'TRANSDATE'])  # .duplicated(keep='last')
# df_final = pd.concat([df_gb1, df_gb2], axis=1)
# df_final.to_csv('kanan.csv')
