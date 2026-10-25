import math
from .figure import GeometricFigure
from .color import FigureColor

class Circle(GeometricFigure):
    FIGURE_NAME = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor(color)

    def area(self):
        return math.pi * (self.radius ** 2)

    @classmethod
    def get_name(cls):
        return cls.FIGURE_NAME

    def __repr__(self):
        return "{}: радиус = {}, цвет = {}, площадь = {:.2f}".format(
            self.get_name(), self.radius, self.color.color, self.area()
        )
