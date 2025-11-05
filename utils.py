import pandas as pd

def readGTRSData(filenames, data_path = "data/raw/metlink_bus/" ):
    if type(filenames) is not list:
        raise TypeError("input need to be in a list")
    return [pd.read_csv(data_path + filename) for filename in filenames]

def writeGTRSData(dataframes, filenames, data_path = "data/processed/metlink_bus/"):
    if type(dataframes) is not list or type(filenames) is not list:
        raise TypeError("input need to be in a list")
    for index, dataframe in enumerate(dataframes):
        dataframe.to_csv(data_path + filenames[index], sep=',', index=False)