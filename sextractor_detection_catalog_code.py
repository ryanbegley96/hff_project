import numpy as np
import pandas as pd

bands = ['f105w','f125w','f140w','f160w','f435w','f606w','f814w']
dataframe_names = ['f105w_df','f125w_df','f140w_df','f160w_df','f435w_df','f606w_df','f814w_df']

def dataframe_maker(band):
    return pd.read_csv('detect_f160w_'+band+'.csv', index=False, sep=',')

for band, name in zip(bands,dataframe_names):
    name = dataframe_maker(band)
    
