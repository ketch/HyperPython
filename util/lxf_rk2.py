# Solution to exercise in Lesson 3.


import sys
sys.path.append('./util')
from ianimate import ianimate
import numpy as np

def f(q):
    return q*(1.0-q)

def minmod(a,b):
    return 0.5*(np.sign(a)+np.sign(b))*np.minimum(np.abs(a),np.abs(b))
    
m = 100      # of points
dx = 1./m   # Size of 1 grid cell
x = np.arange(-3*dx/2, 1.+5*dx/2, dx)

t = 0. # Initial time
T = 0.5 # Final time
dt = 0.4 * dx  # Time step

Q = 0.9*np.exp(-100*(x-0.5)**2)
Qnew = np.zeros(m+4)
Qstar = np.zeros(m+4)
sigma = np.zeros(m+4)

dQplus = np.zeros(m+4)
dQminus = np.zeros(m+4)
F = np.zeros(m+4)
QQ = [Q]

while t < T:
    
    dQplus[:-1] = Q[1:]-Q[:-1]
    dQminus[1:] = Q[1:]-Q[:-1]
    sigma = minmod(dQplus,dQminus)/dx
    
    qplus  = Q[1:-1] - sigma[1:-1] * dx/2.0  # q^+_{i-1/2}
    qminus = Q[:-2]  + sigma[:-2]  * dx/2.0  # q^-_{i-1/2}
    alpha = np.maximum(np.abs(1.-2.*qplus),np.abs(1.-2.*qminus))
    F[1:-1] = 0.5*(f(qplus)+f(qminus) - alpha*dx/dt*(qplus-qminus) )# F_{i-1/2}
    Qstar[2:-2] = Q[2:-2] - dt/dx*(F[3:-1]-F[2:-2])

    Qstar[0:2] = Qstar[2]
    Qstar[-2:] = Qstar[-3]

    dQplus[:-1] = Qstar[1:]-Qstar[:-1]
    dQminus[1:] = Qstar[1:]-Qstar[:-1]
    sigma = minmod(dQplus,dQminus)/dx

    qplus  = Qstar[1:-1] - sigma[1:-1] * dx/2.0  # q^+_{i-1/2}
    qminus = Qstar[:-2]  + sigma[:-2]  * dx/2.0  # q^-_{i-1/2}
    alpha = np.maximum(np.abs(1.-2.*qplus),np.abs(1.-2.*qminus))
    F[1:-1] = 0.5*(f(qplus)+f(qminus) - alpha*dx/dt*(qplus-qminus) )# F_{i-1/2}
    
    Qnew[2:-2] = 0.5*Q[2:-2] + 0.5*(Qstar[2:-2] - dt/dx*(F[3:-1]-F[2:-2]))
    

    Q = Qnew.copy()
    Q[0:2] = Q[2]
    Q[-2:] = Q[-3]
    t = t + dt
    QQ.append(Q)
    
ianimate(x,QQ)
