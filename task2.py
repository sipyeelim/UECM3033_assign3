import numpy as np
import scipy.integrate as spIn
import matplotlib.pyplot as plt

def ode(y,t,a,b):
    y0, y1 = y
    dydt = [a*(y0 - y0*y1),b*(-y1 + y0*y1)]
    return dydt

if __name__ == "__main__":

    # set initial value for y0, y1, a and b
    a = 1.0
    b = 0.2
    y0_a = 0.1
    y1_a = 1.0
    y_a = [y0_a,y1_a]
    # set time range 0 to 5 into 1000 uniform partition
    t = np.linspace(0, 5, 1001)
    #solve nonlinear ODE system
    sol = spIn.odeint(ode,y_a,t,args=(a,b))

    # plotting the graph for both Predator and Prey against Time
    plt.plot(t, sol[:, 0], 'b', label='Prey,y0 against time')
    plt.plot(t, sol[:, 1], 'r', label='Predator,y1 against time')
    plt.title('population against time with y0_a = 0.1')
    plt.legend(loc='best')
    plt.xlabel('time(year)')
    plt.ylabel('population')
    plt.grid()
    plt.show()
    
    # plotting the graph for Predator against Prey
    plt.plot(sol[:, 0],sol[:,1], 'b', label='Predator,y1 against Prey,y0')
    plt.title('Predator,y1 against Prey,y0 with y0_a = 0.1')
    plt.legend(loc='best')
    plt.xlabel('Prey,y0')
    plt.ylabel('Predator,y1')
    plt.grid()
    plt.show()
    

    # Check sensitivity
    # set initial value for y0, y1, a and b
    a = 1.0
    b = 0.2
    y0_b = 0.11
    y1_b = 1.0
    y_b = [y0_b,y1_b]
    # set time range 0 to 5 into 1000 uniform partition
    t = np.linspace(0, 5, 1001)
    #solving the nonlinear ODE system
    sol = spIn.odeint(ode,y_b,t,args=(a,b))

    # plotting the graph for both Predator and Prey against Time
    plt.plot(t, sol[:, 0], 'b', label='Prey,y0 against t')
    plt.plot(t, sol[:, 1], 'r', label='Predator,y1 against t')
    plt.title('population against time with y0_b = 0.11')
    plt.legend(loc='best')
    plt.xlabel('time(year)')
    plt.ylabel('population')
    plt.grid()
    plt.show()
    
    # plotting the graph for Predator against Prey
    plt.plot(sol[:, 0],sol[:,1], 'b', label='Predator,y1 against Prey,y0')
    plt.title('Predator,y1 against Prey,y0 with y0_b = 0.11')
    plt.legend(loc='best')
    plt.xlabel('Prey,y0')
    plt.ylabel('Predator,y1')
    plt.grid()
    plt.show()