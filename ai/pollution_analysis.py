import pandas as pd

# Load sample data
data = pd.read_csv('../data/sample_sensor_data.csv')

# Simple AI filtering (example)
data['PM2.5_filtered'] = data['PM2.5'].rolling(3, min_periods=1).mean()

# Save filtered data
data.to_csv('../data/sample_sensor_data_filtered.csv', index=False)
print("Filtered data saved.")
