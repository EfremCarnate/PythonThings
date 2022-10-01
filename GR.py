import numpy as np 
import matplotlib.pyplot as plt 
import scipy 

from scipy.integrate import solve_ivp 
from scipy.integrate import odeint 

G = 6.67e-11 
pc = 9.2e-27 
C = 8 * np.pi * G * pc 
C = 3 / C 
C = np.sqrt(C) 

m = 0.313 
r = 5.082e-5 
l = 0.686 
 
F = lambda t, s: C * np.sqrt(1/((m * np.exp(-3*t)) + (r * np.exp(-4*t)) + l)) 

t_eval = np.arange(0, 10, 0.01) 
sol = solve_ivp(F, [0, 10], [0], t_eval=t_eval) 

plt.figure(figsize = (12, 4)) 
plt.plot(sol.t, sol.y[0]) 
plt.xlabel('t') 
plt.ylabel('S(t)') 
plt.show() 