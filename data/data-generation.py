import pandas as pd
import numpy as np

n = 1000

data = {
    'temp': np.random.normal(40, 5, n),
    'voltage': np.random.normal(400, 20, n),
    'current': np.random.normal(50, 10, n),
    'mileage': np.random.normal(12000, 3000, n),
    'fault_code': np.random.choice([0, 1], size=n, p=[0.9, 0.1])  # 1 = fault
}

df = pd.DataFrame(data)
df.to_csv('data/synthetic-data.csv', index = False)