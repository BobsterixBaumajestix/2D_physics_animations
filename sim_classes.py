import cv2
import numpy as np
import cv2 as cv


class PointMass:

    def __init__(self, mass, position, velocity, radius, name=None, color=(0, 0, 0), color_norm=255):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.name = name
        self.color = color
        self.color_norm = color_norm

    def normalize_color(self, norm=1, ):
        factor = norm / self.color_norm
        self.color = (self.color[0] * factor, self.color[1] * factor, self.color[2] * factor)
        self.color_norm = norm


# object holding all the point masses and forces
# can update attributes for all point masses collectively

class MassSystem:

    def __init__(self, masses=None, Forces_internal=None, Forces_external=None):
        self.masses = masses
        self.masses_x = np.array([mass.position[0] for mass in self.masses])
        self.masses_y = np.array([mass.position[1] for mass in self.masses])
        self.Forces_int = Forces_internal
        self.Forces_ext = Forces_external

        if self.Forces_int is None:
            self.Forces_int = []
        if self.Forces_ext is None:
            self.Forces_ext = []

    def update_velocities(self, dt):
        for mass_1 in self.masses:
            for force in self.Forces_ext:
                # external force returns vector, in which mass is accelerated
                mass_1.velocity += force(mass_1) / mass_1.mass * dt
            for force in self.Forces_int:
                for mass_2 in self.masses:
                    if np.array_equal(mass_1.position, mass_2.position):
                        continue
                    mass_1.velocity += force(mass_1, mass_2) / mass_1.mass * dt

    def update_positions(self, dt):
        for i in range(len(self.masses)):
            self.masses[i].position += dt * self.masses[i].velocity
            self.masses_x[i] = self.masses[i].position[0]
            self.masses_y[i] = self.masses[i].position[1]

    def visualize(self, imsize, x_range, y_range, rad_scale=1, rad_power=1):

        # initialize image
        out_size = (imsize[0], imsize[1], 3)
        out = np.zeros(out_size, dtype='uint8')
        out.fill(255)

        # set up coordinates
        x_axis = np.linspace(x_range[0], x_range[1], imsize[1])
        y_axis = np.linspace(y_range[0], y_range[1], imsize[0])

        # determine size of pixel in coordinate system
        px_x = abs(x_range[0] - x_range[1]) / imsize[1]
        px_y = abs(y_range[0] - y_range[1]) / imsize[0]

        # print masses on screen
        for mass in self.masses:
            # transform plane coordinates to image array coordinates
            p = mass.position
            x = round((p[0] - x_range[0]) / px_x)
            y = round((y_range[1] - p[1]) / px_y)
            radius = round(rad_scale * np.power(mass.radius / px_x, rad_power))

            # draw point on output image
            out = cv.circle(out, (x, y), radius, mass.color, thickness=-1, lineType=cv2.LINE_AA)

        return out

    def print_status(self):

        print('forces:')
        for force in self.Forces_int:
            print(force)

        print('masses:')
        for mass in self.masses:
            print('name: {}, position: {}, velocity: {}, mass: {}, radius: {}'.format(mass.name, mass.position,
                                                                                      mass.velocity, mass.mass,
                                                                                      mass.radius))
