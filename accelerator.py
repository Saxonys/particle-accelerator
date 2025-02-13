import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#
# Global variables for the accelerator.
# The charge of the particle is based on the elementary charge (Coulombs)
# Mass is equivalent to the scientific weight of a proton used in simulations (mproton​=1.6726219×10−27 kg)
# B_field is the magnet strength of the particle, measured in Tesla, which our value is 1.2 T.
# Voltage is the time step used in the numerical situation. It controls how often the simulation updates.
#

CHARGE = 1.6e-19
MASS = 1.67e-27
B_FIELD = 1.2
VOLTAGE = 1e6
RADIUS = 1.0
TIME_STEP = 1e-9

# Update our physics constants based on the preset global variables.
def update_physics_params():
    global VELOCITY, OMEGA, time, x, y
    VELOCITY = np.sqrt(2 * CHARGE * VOLTAGE / MASS) # Initial velocity from acceleration
    OMEGA = (CHARGE * B_FIELD) / MASS               # Cyclotron frequency
    time = np.linspace(0, 2 * np.pi / OMEGA, 100)   # One full cycle
    x = RADIUS * np.cos(OMEGA * time)
    y = RADIUS * np.sin(OMEGA * time)

update_physics_params()

# Draw out the acceleration figure
fig, ax = plt.subplots()
ax.set_xlim(-RADIUS * 1.2, RADIUS * 1.2)
ax.set_ylim(-RADIUS * 1.2, RADIUS * 1.2)
ax.set_aspect('equal')
ax.set_title("Particle Accelerator Simulation")

# Initialize our particle on the plot, then store it in a list
particle, = ax.plot([], [], 'ro', markersize=8)
particles = [particle]

# Declare the initial velocity for all particles. Makes sure to set initial velocity in x direction.
velocities = [np.array([VELOCITY, 0])]

def init():
    particle.set_data([], [])
    return particle,

#
# This function updates all the particles on the screen.
# We will update the original particle based on its x 
# and y values (its set physic constants in x and y on lines 26 and 27). This
# force is known as the "Lorentz force."
# Then, we will update all the other particles placed by the user with the Lorentz force
# and ensure our new position is a sequence, then return it each time.
# 
def update(frame):
    # Update the original particle (the red one)
    particle.set_data([x[frame]], [y[frame]])

    # Update all the other particles (the ones placed by the user)
    for i, p in enumerate(particles[1:], 1):
        # Apply Lorentz force to each placed particle (same physics as the red one)
        velocity = velocities[i]
        force = np.array([0, CHARGE * B_FIELD * velocity[0]])  # The force due to magnetic field
        acceleration = force / MASS
        velocity += acceleration * TIME_STEP  # The updated velocity
        new_position = np.array([p.get_data()[0][0] + velocity[0] * TIME_STEP, 
                                 p.get_data()[1][0] + velocity[1] * TIME_STEP])

        # Ensure new_position is a sequence (lists)
        p.set_data([new_position[0]], [new_position[1]])
        velocities[i] = velocity  # Store new velocity for the particle

    return particle, *particles[1:]
#
# Create a new particle at the clicked position and start it moving with same velocity as red particle
# It does this by appending the velocity of the red one. 
# 
def on_click(event):
    new_particle, = ax.plot([event.xdata], [event.ydata], 'bo', markersize=8)
    particles.append(new_particle)
    velocities.append(np.array([VELOCITY, 0]))
    ani.event_source.start()  # Just restart animation if it's not running

# We are just drawing the animation using FuncAnimation imported from matplotlib.animation, then waiting
# for the button press event to place another particle on the interface.
ani = animation.FuncAnimation(fig, update, frames=len(time), init_func=init, blit=True, interval=20)
fig.canvas.mpl_connect('button_press_event', on_click)

plt.show()