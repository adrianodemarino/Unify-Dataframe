# Unify dataframe

Unify dataframe is an algorithm written in python that allows to merge 2 dataframe.

Let's image to have 2 dataframe DF1 and DF2. We want a third dataframe DF3 that have to contain the columns and rows of both dataframes and when row and column are shared the value inside the cell will be the sum of these.

<img width="750" alt="Screenshot 2019-03-14 at 15 32 43" src="https://user-images.githubusercontent.com/32490197/54490792-52fd6a80-48b9-11e9-99cd-9d78339cbdc4.png">

## How the algorithm works:
```
def unify_new(list):

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
```
Given a list of a dataframes to merge:
1.  Dictionary is inizialize
2.  For each df:
    *  are stored the values in numpy array,
    *  creation of a tuple (_index_,_column_)
    *  if the tuple not exist in the dictionary
        * the tuple is stored in dictionary with the releated value in the cell of the df
    *  else if the tuple exist in the dictionary
        * the value of the tuple just inserted is update with the sum between the old end the new one.
3.  After these operations, the dictionary will contain all the possible combinations between rows and columns of the all dataframes in the list. 
