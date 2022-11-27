import pandas as pd
from sklearn.preprocessing import Normalizer, MinMaxScaler, MaxAbsScaler, StandardScaler, QuantileTransformer
from sklearn.cluster import KMeans, DBSCAN
from yellowbrick.cluster import KElbowVisualizer

df = pd.read_excel('G:\Python projects\Ofogh_Kurosh\data\Filtered data/RFM values and segments.xlsx')
df1 = df.filter(['recency','frequency','monetary'])

tr1 = DBSCAN()
df_tr1 = tr1.fit_transform(df1)

kmeans = KMeans(n_clusters=7, random_state=0).fit(df_tr1)
# visualizer = KElbowVisualizer(kmeans, k=(4,12))
# visualizer.fit(df_tr1)        # Fit the data to the visualizer
# visualizer.show()        # Finalize and render the figure
df['Cluster'] = kmeans.labels_

df.to_excel('G:\Python projects\Ofogh_Kurosh\data\Filtered data/RFM values and Clusters by KMeans.xlsx')