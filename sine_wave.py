import numpy as np
import matplotlib.pyplot as plt

A = 12
f = 7
phi = 0

t_points = np.array([0.015, 0.035, 0.055, 0.085, 0.120, 0.145, 0.180, 0.215, 0.260, 0.325])

y_points = A * np.sin(2 * np.pi * f * t_points + phi)

print("Manual Computation Verification")
print("-" * 45)
print(f"{'Time (s)':<10}{'Amplitude'}")
for t, y in zip(t_points, y_points):
    print(f"{t:<10.3f}{y:>10.2f}")

t = np.linspace(0, 0.35, 500)
y = A * np.sin(2 * np.pi * f * t + phi)

plt.figure(figsize=(9, 5))
plt.plot(t, y, label='Sine Wave')
plt.scatter(t_points, y_points, color='red', zorder=5, label='Manual Computation Points')

for x, y_val in zip(t_points, y_points):
    plt.text(x, y_val + 0.5, f'({x:.3f}, {y_val:.2f})', ha='center', fontsize=12)

plt.title('Sine Wave: y(t) = 12 sin(2π·7t)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
