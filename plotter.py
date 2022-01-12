import cv2 as cv
import numpy as np


class Figure():
    def __init__(self, name=None, figsize=(400, 400), border=(20, 20), background_color=255, axes=None):
        self.name = name
        self.figsize = figsize
        self.border = border
        height, width = figsize
        self.xaxis = None
        self.yaxis = None
        self.xdata = None
        self.ydata = None


