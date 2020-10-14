#%%
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
#%%
# Scatter points
fig, ax = plt.subplots()
np.random.seed(0)
x, y = np.random.normal(size=(2, 200))
color, size = np.random.random((2, 200))

ax.scatter(x, y, c=color, s=400 * size, alpha=0.3)
ax.grid(color='lightgray', alpha=0.7)
#%%
import matplotlib.pyplot as plt
import mpld3
import numpy
N=100

x=[float(_) for _ in numpy.random.normal(size=N)]
type(x[0])
fig, ax = plt.subplots()
ax.plot(numpy.random.normal(size=N), numpy.random.normal(size=N), 'o', alpha=0.3)
ax.set_title("My Plot", size=20)
labels = ['point {0}'.format(i + 1) for i in range(100)]
mpld3.display(fig)
#%%
df = pd.DataFrame({'B': [0, 1, 2, np.nan, 4]})
#%%
df.rolling(2, win_type='triang').sum()