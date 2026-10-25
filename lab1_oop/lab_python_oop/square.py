from .rectangle import Rectangle

class Square(Rectangle):
    
    FIGURE_NAME = "Квадрат"

    def __init__(self, side_length, color):
        super().__init__(width=side_length, height=side_length, color=color)

    @classmethod
    def get_name(cls):
        return cls.FIGURE_NAME

    def __repr__(self):
        return "{}: сторона = {}, цвет = {}, площадь = {:.2f}".format(
            self.get_name(), self.width, self.color.color, self.area()
        )
