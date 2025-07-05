
def model_v6_6_logic(df):
    cond1 = df['Volume'] > df['Volume'].rolling(3).mean()
    cond2 = df['Price_Change_Pct'] > 0
    cond3 = df['Rolling_Avg_5'] < df['Close']
    return cond1 & cond2 & cond3
