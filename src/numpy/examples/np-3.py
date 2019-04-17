#asarray function is like array
#it can create an ndarray from list,tuple etc
import numpy as np;
list=[10,20,30];
tuple=(40,50,60,70);
npa1=np.asarray(list);
npa2=np.asarray(tuple);
npa3=np.asarray(tuple,dtype=float);
print(npa1);
print(npa2);
print(npa3);
