import pandas as pd

def generate_features(df):
    df['Volume_Change'] = df['Volume'].pct_change().fillna(0)
    df['Price_Change'] = df['Close'] - df['Open']
    df['Price_Change_Pct'] = df['Price_Change'] / df['Open']
    df['Is_Bullish'] = (df['Close'] > df['Open']).astype(int)
    df['Rolling_Avg_5'] = df['Close'].rolling(5).mean().fillna(method='bfill')
    return df