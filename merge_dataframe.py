import pandas as pd
import numpy as np

def unify(list):

    super = {}

    for df in list:
        value = df.values
        for n,i in enumerate(df.index):
            for k,j in enumerate(df.columns):
                if j in super:
                    if i in super[j]:
                        super[j][i] += value[n,k]
                    else:
                        super[j][i] = value[n,k]
                else:
                    super[j] = {i : value[n,k]}

    return pd.DataFrame.from_dict(super)

list = [ df_1,df_2 ] 

new_df = unify(list)
