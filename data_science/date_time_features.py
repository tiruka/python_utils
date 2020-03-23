def datetime_feature_engineering(df, time_col):
    '''
    Extract feature from datetime by convertint to hour.
    Inputs are df (pandas.DataFrame) and time_col which will be conveted into the below.
    The time_col must be dtype: datetime64[ns].
    For example, '2020-03-05 15:10:51' 
    hour -> 15
    minute -> 10
    day_of_month -> 8
    day_of_week -> 3 (Thursday. Monday=0, Sunday=6)
    week -> 1 (first week of the month)
    month -> 3
    quarter -> 1 
    week_of_year -> 10
    
    Use case:
    df = datetime_feature_engineering(df, 'start_time')
    then, colums will be added.
    '''
    df['hour'] =  df[time_col].apply(lambda x: x.hour)
    df['minute'] =  df[time_col].apply(lambda x: x.minute)
    df['day_of_month'] =  df[time_col].apply(lambda x: x.day)
    df['day_of_week'] =  df[time_col].apply(lambda x: x.dayofweek)
    df['week'] =  df[time_col].apply(lambda x: x.week)
    df['month'] =  df[time_col].apply(lambda x: x.month)
    df['quarter'] =  df[time_col].apply(lambda x: x.quarter)
    df['week_of_year'] =  df[time_col].apply(lambda x: x.weekofyear)
    return df