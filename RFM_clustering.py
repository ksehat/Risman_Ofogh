import pandas as pd
from sklearn.preprocessing import Normalizer, MinMaxScaler, MaxAbsScaler, StandardScaler, QuantileTransformer
from sklearn.cluster import KMeans, DBSCAN
from yellowbrick.cluster import KElbowVisualizer

chunk = pd.read_csv('G:\Python projects\Ofogh_Kurosh\data\Filtered data/Min_MAX_by month.csv',chunksize=1000)
df = pd.concat(chunk)
df = df[df['NetAmount'] > 0]
df1 = df.filter(['freq_month','NetAmount','Min','Max','Median'])

tr1 = Normalizer()
df_tr1 = tr1.fit_transform(df1)

kmeans = KMeans(n_clusters=7, random_state=0).fit(df_tr1)
# dbscan = DBSCAN(eps=0.5,min_samples=1).fit(df_tr1)

visualizer = KElbowVisualizer(kmeans, k=(4,12))
visualizer.fit(df_tr1)        # Fit the data to the visualizer
visualizer.show()        # Finalize and render the figure

# df['Cluster'] = kmeans.labels_
#
# df.to_csv('G:\Python projects\Ofogh_Kurosh\data\Filtered data/info_min_max Clusters by KMeans.csv')