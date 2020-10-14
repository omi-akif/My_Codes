import pandas as pd
import numpy as np 

df = pd.DataFrame(
    {
        'A':[1,2,np.nan],
        'B':[5,np.nan,np.nan],
        'C':[1,2,3]
    }
)
print(df)