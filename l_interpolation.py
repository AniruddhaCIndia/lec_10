import numpy as np
X1=[0,1,2] #the set of x values
X=np.array(X1)
Y1=[1,2,4] #the set of corresponding y values for the unknown function
Y=np.array(Y1)
x=float(input("give the value of x at which the functional value needs to be found: "))
sum=0

for i in range (len(X)):
    term=1
    for j in range (len(X)):
        if j!=i:
            term=term*(x-X[j])/(X[i]-X[j])
    sum=sum+term*Y[i]
print(sum)

a=2*2**0.5
print("The exact value is : ",a)
