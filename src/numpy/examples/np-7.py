#basic operatiosn on single array

import numpy as np;

ar=np.array([10,20,30,40,50,60]);

ar1=ar+1;   #adding 1 to each element   
print(ar1);
print("______________________________________________________________________");

ar2=ar-1;   #subtracting 1 from each element
print(ar2);
print("______________________________________________________________________");

ar3=ar*2;   #multiplying 2 to each element
print(ar3);
print("______________________________________________________________________");

ar4=ar/2;   #dividing each element by 2   
print(ar4);
print("______________________________________________________________________");

#basic operation on 2d array

ar5=np.array([[20,30],[40,50]]); #adding 
ar6=ar5+1;
print(ar6);
print("______________________________________________________________________");
ar7=ar5-1;  #sutracting each element by 2
print(ar7);
print("______________________________________________________________________");
ar8=ar7.T;  #transpose of an matrix (row to col and cols to row)
print(ar8); 
