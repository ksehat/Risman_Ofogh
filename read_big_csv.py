# import required modules
import pandas as pd
import numpy as np
import time
# import sklearn

# time taken to read data
s_time_chunk = time.time()
chunk = pd.read_csv('G:\Python projects\Ofogh_Kurosh\data\Filtered data/1400.csv', chunksize=1000, delimiter='|')
chunk1 = pd.read_csv('G:\Python projects\Ofogh_Kurosh\data\Filtered data/1401.csv', chunksize=1000, delimiter='|')
df = pd.concat(chunk)
df1 = pd.concat(chunk1)
df_final = pd.concat([df,df1])
df_final.to_csv('G:\Python projects\Ofogh_Kurosh\data\Filtered data/1400_1401.csv')
e_time_chunk = time.time()
print("With chunks: ", (e_time_chunk - s_time_chunk), "sec")

