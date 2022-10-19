# function that takes a csv files and retrun a dataframe
def get_dataframe(filename):
    import pandas as pd
    df = pd.read_csv(filename)
    return df
