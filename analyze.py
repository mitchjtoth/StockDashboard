import pandas as pd


def cleanData(data, symbol):
    # create pandas dataframe with the data
    df = pd.DataFrame(data)
    
    # swap the rows and columns
    df = df.transpose()
    
    # move the dates into their own column and index the table
    df = df.reset_index()

    # rename the columns
    df.columns = ["date", "open", "high", "low", "close", "volume"]
    
    # convert the data types from strings
    df = df.astype({'open': 'float64', 'high': 'float64', 'low': 'float64', 'close': 'float64', 'volume': 'float64'})
    
    # change the datatype of the dates to datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # sort the table by the dates in ascending order
    df = df.sort_values(by='date')
    print(df.head())

    # save the data in a csv
    df.to_csv(f"data/{symbol}_cleaned.csv", index=False)
    
    return df