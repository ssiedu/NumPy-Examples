#indexing in nparray
import numpy as np;

ar1=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]);
print(ar1);

#slicing an array
ar2=ar1[0:2, 0:3];  #slicing 0,1 row and 0,1,2 cols  
print(ar2);
print("_________________________________________________________________");
ar3=ar1[[0, 1, 2], [2, 1, 0]]   #(0,2),(1,1),(2,0) 
print(ar3);#[3,6,9]
print("_________________________________________________________________");
ar4=ar1[ar1>5]; #will fetch elements which satisfies the condition [6,7,8,9,10,11,12] will be result
print(ar4);