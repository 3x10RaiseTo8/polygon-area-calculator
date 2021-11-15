class Rectangle:
    def __init__(self, w=0, h=0):
        self.width = w
        self.height = h

    def set_width(self, w): self.width = w
    def set_height(self, h): self.height = h

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'
        picture = ''
        for r in range(self.height):
            picture += '*' * self.width + '\n'
        return picture

    def get_amount_inside(self, shape):
        area = self.get_area()
        shapearea = shape.get_area()
        return int(area / shapearea)

    def __repr__(self):
        return 'Rectangle(width={}, height={})'.format(self.width, self.height)


def setboth(self, s):
    self.height = s
    self.width = s


class Square(Rectangle):
    def __init__(self, s=0): setboth(self, s)
    def set_side(self, s): setboth(self, s)
    def set_width(self, s): setboth(self, s)
    def set_height(self, s): setboth(self, s)

    def __repr__(self):
        return 'Square(side={})'.format(self.width)
