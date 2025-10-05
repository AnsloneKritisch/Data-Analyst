# Many times the data is unbalanced. In this case we need to handle this data.
# Because then the information will be more in the favour of the majority class
# Just to balance it so that the information is more in the favour of both 
# There are 2 ways - undersampling and Downsampling

# 🔽 Downsampling (Reducing Data Size)
# Meaning: You reduce the number of rows by converting higher frequency data (like hourly) to lower frequency (like daily or weekly).

# ✅ Why?
# To summarize data

# To reduce size for analysis

# To make trends easier to see

# 📌 Example:
# Let’s say you have temperature data every hour, and you just want to see daily average temperature.

import pandas as pd
import numpy as np

# Create hourly data for 2 days
date_rng = pd.date_range(start='2025-01-01', end='2025-01-02 23:00', freq='h')
data = np.random.randint(15, 35, size=(len(date_rng)))  # random temperatures
df = pd.DataFrame(data, index=date_rng, columns=['Temperature'])

# Downsample: hourly → daily (mean temperature)
daily_avg = df.resample('D').mean()

print(daily_avg)
