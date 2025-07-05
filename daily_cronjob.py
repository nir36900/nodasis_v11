from floor_sheet_loader import load_from_csv
from feature_generator import generate_features

df = load_from_csv("data/floor_sheet.csv")
df = generate_features(df)
df.to_csv("data/processed.csv", index=False)
print("Daily processing complete.")