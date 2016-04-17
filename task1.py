import numpy as np
import sympy as sy
#Your optional code here
#You can import some modules or create additional functions

# DO NOT CHANGE THE NAME OF gausslegendre() function
def gausslegendre(f, a, b, n=20):
    ans = 0
    # Edit here to implement your code
    #Legendre function used to obtain the node and weights from n = 1 until 100 
    x,weight = np.polynomial.legendre.leggauss(n)
 #By using Lagrange polynomial to transform the definite integral into the range from -1 to 1
    y = a*((x-1)/(-1-1)) + b*((x+1)/(1+1))  
# use jacabian of the transformation which is (b-a)/2
    ans = ((b-a)/2) * np.dot(f(y),np.transpose(weight))

    return ans

if __name__ == "__main__":
    def f(x):
        return (x**2 +7*x)/(1 +np.sqrt(x))**4
    
    def my_integral():
        x = sy.Symbol('x')
        ans = sy.integrate((x**2 +7*x)/(1 +sy.sqrt(x))**4, (x,0, 1))
        return ans
    
    print('Answer:                    I = ', my_integral())
    print('Your implementation gives: I = ', gausslegendre(f, 0,1))