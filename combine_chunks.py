import pandas as pd
import glob

# Combine all CSVs in the folder
csv_files = glob.glob("2025_csv/*.csv")
combined_df = pd.concat([pd.read_csv(f) for f in csv_files], ignore_index=True)

# Save combined data
combined_df.to_csv("combined_data.csv", index=False)
