import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.preprocessing import Normalizer, MinMaxScaler, MaxAbsScaler, StandardScaler, QuantileTransformer

df = pd.read_excel('G:\Python projects\Ofogh_Kurosh\data\Filtered data/RFM values and segments.xlsx')

tr1 = Normalizer()
tr2 = MaxAbsScaler()
tr3 = MinMaxScaler()
tr4 = StandardScaler()
tr5 = QuantileTransformer()

df_for_normalization = df.drop(columns=['Information','Segment'])
df_tr1 = pd.DataFrame(tr1.fit_transform(df_for_normalization),columns=['recency','frequency','monetary'])
df_tr2 = pd.DataFrame(tr2.fit_transform(df_for_normalization),columns=['recency','frequency','monetary'])
df_tr3 = pd.DataFrame(tr3.fit_transform(df_for_normalization),columns=['recency','frequency','monetary'])
df_tr4 = pd.DataFrame(tr4.fit_transform(df_for_normalization),columns=['recency','frequency','monetary'])
df_tr5 = pd.DataFrame(tr5.fit_transform(df_for_normalization),columns=['recency','frequency','monetary'])
df_tr1['Segment'] = df['Segment']
df_tr2['Segment'] = df['Segment']
df_tr3['Segment'] = df['Segment']
df_tr4['Segment'] = df['Segment']
df_tr5['Segment'] = df['Segment']
# df.drop(df.index[df['monetary'] <= 0],inplace=True)
# df['monetary for size'] = np.log2(df['monetary'])

dict_trans = {
     'Normalizer': df_tr1,
     'MaxAbsScaler': df_tr2,
     'MinMaxScaler': df_tr3,
     'StandardScaler': df_tr4,
     'QuantileTransformer': df_tr5,
}

for k in dict_trans:
    fig = px.scatter_3d(dict_trans[k], x='recency', y='frequency', z='monetary',
                    color='Segment',
                    # size='monetary for size',
                    title="3D Scatter Plot")
    fig.update_traces(marker_size = 2)
    # fig.show()
    fig.write_html(f'G:\Python projects\Ofogh_Kurosh\data\Filtered data/RFM values and segments_transformation_{k}_wo_color.html')