#binary operations on array

import numpy as np;

#for single dimensions
sdA=np.array([10,20,30,40]);
sdB=np.array([5,6,7,8]);
print(sdA+sdB);#will add 10+5, 20+6, 30+7 (size must be same)
print(sdA-sdB);#will sub
print(sdA*sdB);#will multiply
print(sdA/sdB);#will divide


#for multi dimensions
mdA=np.array([[10,20,30],[40,50,60],[70,80,90]]);
mdB=np.array([[1,2,3],[4,5,6],[7,8,9]]);
print(mdA+mdB); #overloaded operators (same task we can do with methods like add,subtract,multiply,divide)
print(np.add(mdA,mdB));
print(mdA-mdB);
print(mdA*mdB); #array multiplication
print(mdA.dot(mdB)); #matrix multiplication
print(np.sqrt(mdA));    #square root of each element
print(np.square(mdA));  #square of each element
