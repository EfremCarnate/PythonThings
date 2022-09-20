import numpy as np 
import matplotlib.pyplot as plt 
import scipy 

from scipy.integrate import solve_ivp 
from scipy.integrate import odeint 

F = lambda t, s: np.cos(t) + np.sin(t) 
e = 2 * np.pi

t_eval = np.arange(0, e, 0.01) 
sol = solve_ivp(F, [0, e], [0], t_eval=t_eval) 

plt.figure(figsize = (12, 4)) 
plt.plot(sol.t, sol.y[0]) 
plt.xlabel('t') 
plt.ylabel('S(t)') 
plt.show() 