# import required modules
import pandas as pd
import numpy as np
import time

# time taken to read data
s_time_chunk = time.time()
chunk = pd.read_csv('G:\Python projects\Ofogh_Kurosh\data\Filtered data/1400.csv', chunksize=1000)
e_time_chunk = time.time()

print("With chunks: ", (e_time_chunk - s_time_chunk), "sec")
df = pd.concat(chunk)

# data
df.sample(10)