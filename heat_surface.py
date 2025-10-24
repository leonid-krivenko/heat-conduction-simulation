import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Tau = 0.45                      
L = 0.4                         
dx = 0.01                        
alpha = 0.000097                 
dt = Tau * dx**2 / alpha         
Nx = int(L / dx) + 1             
t_total = L**2 / alpha          
Nt = int(t_total / dt)         
T_outside = 350.0                
T_initial = 28.0                

T = np.ones(Nx) * T_initial
T[0] = T_outside

T_evolution = np.zeros((Nt, Nx))
T_evolution[0, :] = T

for n in range(1, Nt):
    T_new = T.copy()
    for i in range(1, Nx - 1):
        T_new[i] = T[i] + alpha * dt / dx**2 * (T[i+1] - 2*T[i] + T[i-1])

    T_new[0] = T_outside     
    T_new[-1] = T_new[-2]     
    T = T_new
    T_evolution[n, :] = T


x = np.linspace(0, L, Nx)                      
t_sec = np.linspace(0, dt * Nt, Nt)           
t_min = t_sec / 60                           
X, T_mesh = np.meshgrid(x, t_min)             

fig = plt.figure(figsize=(11, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T_mesh, T_evolution, cmap='viridis')

ax.set_xlabel('Distance (meters)')
ax.set_ylabel('Time (minutes)')
ax.set_zlabel('Temperature (°C)')
ax.set_title('Temperature Evolution in Aluminum Rod Over Time')
plt.tight_layout()
plt.show()

points_cm = [4.0, 21.5, 38.0]  
indices = [int(round(p / 100 / dx)) for p in points_cm]  

plt.figure(figsize=(9, 6))
for idx, dist_cm in zip(indices, points_cm):
    plt.plot(t_min, T_evolution[:, idx], label=f'{dist_cm} cm')

plt.xlabel('Time (minutes)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature at Selected Points in Rod Over Time')
plt.legend(title='Distance from heat source (cm)', loc='lower right')
plt.grid(True)
plt.tight_layout()
plt.show()

print(f"Simulated total time: {t_total:.2f} seconds ≈ {t_total / 60:.2f} minutes")
print(f"Time step dt = {dt:.5f} s, Number of steps Nt = {Nt}")
