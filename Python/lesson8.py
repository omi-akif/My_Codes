import numpy as np
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
x=np.linespace(1,5,10)
y = x**2
plt.plot(x,y, "red", linewidth=1,markersize=10, marker= "+")
plt.xlabel("XLabel")
plt.ylabel("Y Label")
plt.title("First Chart")
plt.show()