import numpy as np
from sim_classes import PointMass, MassSystem
import forces


# POINT MASSES

# solar system masses
sun = PointMass(mass=1.989e30, position=np.array([0., 0.]), velocity=np.array([0., 0.]), radius=696340000, name='sun',
                color=(242, 219, 15), color_norm=255)

mercury = PointMass(mass=0.330e24, position=np.array([57.9e9, 0.]), velocity=np.array([0., -47.4e3]), radius=4879e3,
                    name='mercury', color=(197, 230, 235), color_norm=255)

venus = PointMass(mass=4.87e24, position=np.array([108.2e9, 0.]), velocity=np.array([0., -35.0e3]), radius=12104e3,
                  name='venus', color=(14/255, 208/255, 234/255), color_norm=255)

earth = PointMass(mass=5.97e24, position=np.array([149.6e9, 0.]), velocity=np.array([0., -29.8e3]), radius=12756e3,
                  name='earth', color=(255/255, 127/255, 0/255), color_norm=255)

mars = PointMass(mass=0.642e24, position=np.array([228.0e9, 0.]), velocity=np.array([0., -24.1e3]), radius=6792e3,
                 name='mars', color=(9., 127., 244.), color_norm=255)

jupiter = PointMass(mass=1898e24, position=np.array([778.5e9, 0.]), velocity=np.array([0., -13.1e3]), radius=142984e3,
                    name='jupiter', color=(11/255, 112/255, 237/255), color_norm=255)

saturn = PointMass(mass=568e24, position=np.array([1432.0e9, 0.]), velocity=np.array([0., -9.7e3]), radius=120536e3,
                   name='saturn', color=(11/255, 74/255, 158/255), color_norm=255)

uranus = PointMass(mass=86.8e24, position=np.array([2867.0e9, 0.]), velocity=np.array([0., -6.8e3]), radius=51118e3,
                   name='uranus', color=(145/255, 247/255, 2/255), color_norm=255)

neptune = PointMass(mass=102.e24, position=np.array([4515.0e9, 0.]), velocity=np.array([0., -5.4e3]), radius=49528e3,
                    name='neptune', color=(247/255, 137/255, 2/255), color_norm=255)


# masses organized in a circle, central mass
angle = 2 * np.pi / 8

central_mass = PointMass(mass=50, position=np.array([0., 0.]), velocity=np.array([0., 0.]), radius=0.2,
                         name='central_mass', color=(255, 0, 0))
mass_1 = PointMass(mass=1, position=np.array([np.cos(angle * 0), np.sin(angle * 0)]), velocity=np.array([0., 0.]),
                   radius=0.05, name='mass_1',
                   color=(0, 0, 255))
mass_2 = PointMass(mass=1, position=np.array([np.cos(angle * 1), np.sin(angle * 1)]), velocity=np.array([0., 0.]),
                   radius=0.05, name='mass_2',
                   color=(0, 0, 255))
mass_3 = PointMass(mass=1, position=np.array([np.cos(angle * 2), np.sin(angle * 2)]), velocity=np.array([0., 0.]),
                   radius=0.05, name='mass_3',
                   color=(0, 0, 255))
mass_4 = PointMass(mass=1, position=np.array([np.cos(angle * 3), np.sin(angle * 3)]), velocity=np.array([0., 0.]),
                   radius=0.05, name='mass_4',
                   color=(0, 0, 255))
mass_5 = PointMass(mass=1, position=np.array([np.cos(angle * 4), np.sin(angle * 4)]), velocity=np.array([0., 0.]),
                   radius=0.05, name='mass_5',
                   color=(0, 0, 255))
mass_6 = PointMass(mass=1, position=np.array([np.cos(angle * 5), np.sin(angle * 5)]), velocity=np.array([0., 0.]),
                   radius=0.05, name='mass_6',
                   color=(0, 0, 255))
mass_7 = PointMass(mass=1, position=np.array([np.cos(angle * 6), np.sin(angle * 6)]), velocity=np.array([0., 0.]),
                   radius=0.05, name='mass_7',
                   color=(0, 0, 255))
mass_8 = PointMass(mass=1, position=np.array([np.cos(angle * 7), np.sin(angle * 7)]), velocity=np.array([0., 0.]),
                   radius=0.05, name='mass_8',
                   color=(0, 0, 255))


# MASS SYSTEM setups

# solar system
sun_earth = {'name': 'sun-earth system',
             'system': MassSystem(masses=[sun, earth], Forces_internal=[forces.gravity]),
             'window_size': (800, 800),
             'x_range': (-160.e9, 160.e9),
             'y_range': (-160.e9, 160.e9),
             'dt': 60 * 60 * 24,
             'wait': 0.01}

solar_system = {'name': 'solar system',
                'system': MassSystem(masses=[sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune],
                                     Forces_internal=[forces.gravity]),
                'window_size': (800, 800),
                'x_range': (-4520.0e9, 4520.0e9),
                'y_range': (-4520.0e9, 4520.0e9),
                'dt': 60 * 60 * 24 * 10,
                'wait': 0.01}

solar_system_inner = {'name': 'solar system',
                      'system': MassSystem(masses=[sun, mercury, venus, earth],
                                           Forces_internal=[forces.gravity]),
                      'window_size': (800, 800),
                      'x_range': (-160.e9, 160.e9),
                      'y_range': (-160.e9, 160.e9),
                      'dt': 60 * 60 * 24,
                      'wait': 0.01}

solar_system_outer = {'name': 'solar system',
                      'system': MassSystem(masses=[sun, mars, jupiter, saturn, uranus, neptune],
                                           Forces_internal=[forces.gravity]),
                      'window_size': (800, 800),
                      'x_range': (-4520.0e9, 4520.0e9),
                      'y_range': (-4520.0e9, 4520.0e9),
                      'dt': 60 * 60 * 24 * 30,
                      'wait': 0.01}


# harmonic oscillator
harmonic_oscillator_complex = {'name': 'harmonic oscillator',
                               'system': MassSystem(
                                   masses=[central_mass, mass_1, mass_2, mass_3, mass_4, mass_5, mass_6, mass_7,
                                           mass_8],
                                   Forces_internal=[forces.harmonic_oscillator]),
                               'window_size': (800, 800),
                               'x_range': (-3, 3),
                               'y_range': (-3, 3),
                               'dt': 0.01,
                               'wait': 0.01}

harmonic_oscillator_simple = {'name': 'harmonic oscillator',
                              'system': MassSystem(masses=[mass_1, mass_2],
                                                   Forces_internal=[forces.harmonic_oscillator]),
                              'window_size': (800, 800),
                              'x_range': (-2, 2),
                              'y_range': (-2, 2),
                              'dt': 0.01,
                              'wait': 0.01}
