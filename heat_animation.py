import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

Tau = 0.45
L = 0.3
dx = 0.01
alpha = 0.00582
dt = Tau * dx**2 / alpha
Nx = int(L / dx) + 1
С = 1
t_total = С * L**2 / alpha
Nt = int(t_total / dt)
T_outside = 500
T_initial = 20.0

T = np.ones(Nx) * T_initial
T[0] = T_outside

T_evolution = np.zeros((Nt, Nx))
T_evolution[0, :] = T

for n in range(1, Nt):
    T_new = T.copy()
    for i in range(1, Nx - 1):
        T_new[i] = T[i] + alpha * dt / dx**2 * (T[i + 1] - 2 * T[i] + T[i - 1])
    T_new[0] = T_outside
    T_new[-1] = T_new[-2]
    T = T_new
    T_evolution[n, :] = T

x = np.linspace(0, L, Nx)

fig, ax = plt.subplots(figsize=(8, 4))
line, = ax.plot(x, T_evolution[0, :], color='red')
ax.set_ylim(T_initial, T_outside + 100)
ax.set_xlim(0, L)
ax.set_xlabel('Distance (m)')
ax.set_ylabel('Temperature (°C)')
ax.set_title('Temperature Profile Over Time')

def update(frame):
    line.set_ydata(T_evolution[frame, :])
    ax.set_title(f'Time: {frame * dt:2f} min')
    return line,

ani = FuncAnimation(fig, update, frames=range(0, Nt, max(1, Nt // 200)), interval=30)
plt.close(fig)  
HTML(ani.to_jshtml())

