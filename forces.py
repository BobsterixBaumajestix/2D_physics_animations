import numpy as np
import vector_tools


def gravity(mass_1, mass_2):
    # gravitational force exerted by mass_2 onto mass_1

    # gravitational constant
    G = 6.67408e-11

    distance = np.linalg.norm(mass_1.position - mass_2.position)
    F_g = (G * mass_1.mass * mass_2.mass / distance ** 2)
    r = vector_tools.normalized_connection_vector(start=mass_1.position, end=mass_2.position)
    return F_g * r


def harmonic_oscillator(mass_1, mass_2, k=5):
    distance = np.linalg.norm(mass_1.position - mass_2.position)
    F = (k * distance)
    r = vector_tools.normalized_connection_vector(start=mass_1.position, end=mass_2.position)
    return F * r


def earth_grav_field(mass):
    g = 9.807
    F_g = mass.mass * g * np.array([0., -1.])
    return F_g


def fixed_harmonic_oscillator(mass, fixpoint=np.array([0., 0.]), k=10):
    if np.array_equal(mass.position, fixpoint):
        return np.array([0., 0.])
    r = vector_tools.normalized_connection_vector(start=mass.position, end=fixpoint)
    d = np.linalg.norm(mass.position - fixpoint)
    F = k * d
    return F * r


def spring_pendulum(mass, fixpoint=np.array([0., 0.]), k=20, length=1):
    d = np.linalg.norm(mass.position - fixpoint)
    if d > length:
        r = vector_tools.normalized_connection_vector(start=mass.position, end=fixpoint)
        F = k * d
        return F * r
    else:
        return np.array([0., 0.])
