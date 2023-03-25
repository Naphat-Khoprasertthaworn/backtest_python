import pandas as pd
import numpy as np
import globals


class Database:
    __df = pd.DataFrame()

    def __init__(self, file_path):
        self.__df = pd.read_csv(file_path,names=['DateTime','Bid','Ask','Volume'],header=None)

    def get_data_frame(self):
        return self.__df

    def get_df_index(self,index):
        if index > globals.global_index or index < 0:
            return False
        return self.__df.iloc[[index]]

    def get_df_period(self,start,stop):
        if stop > globals.global_index+1 or start > stop or start < 0 or stop < 0:
            return False
        return self.__df.iloc[start:stop]


