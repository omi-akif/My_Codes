#%%
from rpy2.robjects import r, pandas2ri
def data(name):
    return pandas2ri.ri2py(r[name])