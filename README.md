# Particle Accelerator Simulation

This repository contains a simulation of a particle accelerator where particles are accelerated by a magnetic field, following the principles of cyclotron motion. The simulation simulates the trajectory of charged particles and animate their motion in a 2D plane.

### Description

The simulation shows how charged particles (like protons or electrons) move in a circular path under the influence of a magnetic field, which is a typical setup in a **cyclotron** or other types of particle accelerators.

- A **red particle** starts moving in a circular path based on the specified physical constants (such as charge, mass, voltage, etc.).
- The particles interact with the magnetic field, updating their positions based on the **Lorentz force**.

### Physical Constants

The simulation is based on these typical values for particle motion:

  - **Charge (CHARGE)**: The elementary charge (1.6 times 10^{-19} Coulombs).
  - **Mass (MASS)**: The mass of a proton (1.67 times 10^{-27} kg).
  - **Magnetic Field Strength (B_FIELD)**: (1.2 Tesla).
  - **Voltage (VOLTAGE)**: (1 times 10^{6} Volts or 1 Megavolt).
  - **Radius (RADIUS)**: The radius of the particle's circular motion, set to 1.0 meter.
  - **Time Step (TIME_STEP)**: The time step used in the simulation, set to (1 times 10^{-9} seconds).

Simpler explanations for these values can be found in the comments of the code.

### Features

  - **Cyclotron Motion**: The simulation visually demonstrates how charged particles move in a circular path under the influence of a magnetic field.
  - **Real-Time Animation**: Particles move in real-time according to their physical behavior, updating their position and velocity with each frame.
  - **User Interaction**: Clicking on the plot adds additional particles that move in the same manner as the original red particle. Users can extend, shrinken, move, and save the graph as a PNG.

## How to Run

### Requirements

You can install the necessary libraries using pip:

```bash
pip install matplotlib numpy
