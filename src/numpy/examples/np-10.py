#sorting numpy array

import numpy as np;
#single dim array
sd=np.array([100,20,45,90,44,10,25]);
print(np.sort(sd)); #sorting in ascending order
print(np.sort(sd)[::-1]);#sorting and slicing in reverse direction (desc order)
print("__________________________________________________________");
md=np.array([[20,10,5],[40,22,34],[90,94,2]]);
print(md);
print(np.sort(md));#will sort the rows
print(md);
print(np.sort(md,axis=None));#will sort and generate list of sorted element
print(np.sort(md,axis=1));#will sort row wise
print(np.sort(md,axis=0));#will sort column wise






