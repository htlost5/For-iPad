import numpy as np
from scipy.integrate import solve_ivp

def velocity_with_air_resistance(mass, height, air_density=1.225, drag_coefficient=0.47, area=1.0):
    # Constants
    g = 9.81  # gravity acceleration (m/s^2)
    
    # Air resistance function
    def equations(t, y):
        v = y[0]
        drag_force = 0.5 * air_density * drag_coefficient * area * v**2
        dvdt = (mass * g - drag_force) / mass
        return [dvdt]

    # Initial conditions: starting from rest
    y0 = [0]

    # Time to fall from the given height
    t_span = (0, np.sqrt(2 * height / g))

    # Solve the differential equation
    sol = solve_ivp(equations, t_span, y0, method='RK45', t_eval=[t_span[1]])

    return sol.y[0][-1]

# Example usage
mass = input("質量(kg)：")  # kg
height = input("高さ(m)：")  # meters

# Calculate final velocity in m/s
final_velocity_mps = velocity_with_air_resistance(mass, height)

# Convert to other units
final_velocity_mpm = final_velocity_mps * 60  # meters per minute
final_velocity_kph = final_velocity_mps * 3.6  # kilometers per hour

# Print results in a table format
print("\nFinal Velocity:")
print(f"{'Unit':<20}{'Velocity'}")
print(f"{'-'*30}")
print(f"{'秒速 ':<20}{final_velocity_mps:.1f}"+"m/s")
print(f"{'分速 ':<20}{final_velocity_mpm:.1f}"+"m/min")
print(f"{'時速 ':<20}{final_velocity_kph:.1f}"+"km/h")